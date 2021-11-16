import telebot # importing pyTelegramBotApi
import requests
import json

# For latest version checkout: https://github.com/w3Abhishek/UrbanDictionaryBot
# UrbanDictionayBot is using http://api.urbandictionary.com/v0/define?term=flump API (Unofficial)

bot = telebot.TeleBot('2107309460:AAEXty9oV7YY69bprPKUkdKE6yioyv2Ngvg') # replace TOKEN with your bot token to authorize your bot

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

@bot.message_handler(commands=['ud']) # command to trigger the function
def start(message):
    try:
        word = message.text[3:] # get the word from the message
        url = 'http://api.urbandictionary.com/v0/define?term=%s' % (word) # url to get the definition
        response = requests.get(url, headers=headers) # get the response from the url
        data = response.json() # get the data from the response
        example = data['list'][0]['example'] # get the example from the data
        example = example.replace('\r\n', '\n') # replace the \r\n with \n
        example = example.replace('[', '') # removes [
        example = example.replace(']', '') # removes ]
        final_message = 'Definition:\n\n%s\n\n---\n\nExample: %s\n\nSource: Urban Dictionary\n\nRequested by %s'% (data['list'][0]['definition'], example, message.from_user.first_name) # final message
        bot.reply_to(message, final_message, parse_mode='Markdown', disable_web_page_preview=True) # reply to the message with the definition
    except: # if the word is not found
        bot.reply_to(message, "No Meaning Available") # reply to the message if the word is not found

bot.polling() # start the bot
