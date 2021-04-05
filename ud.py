import json
import requests
import telebot

# Enter Your Bot Token in place of TOKEN
bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['ud']) # /ud command will invoke this function
def send_welcome(message):
    # Picking the requested word from Telegram message
    givenQuery = message.text[4:]
    
    if (givenQuery != ""): # Condition ensures that some query is passed with command /ud
        # Passing Query to Urban Dictionary API
        queryResponse = requests.get("http://api.urbandictionary.com/v0/define?term=" + givenQuery)
        udResponse = json.loads(queryResponse.text) # Loads the json response in Text format and then passes to udResponse variable

        if(udResponse['list'] != []): # Check whether response is empty or not
            finalMessage = str("Meaning of " + givenQuery) + str("\n\n" + udResponse['list'][0]['definition']) + str("\n\nExample: " + udResponse['list'][0]['example'])
            finalMessage.replace("[","") # Removes '[]' from finalMessage before sending
            finalMessage.replace("]","")
            bot.reply_to(message, finalMessage)
        else:
            bot.reply_to(message, "No meaning available on Urban Dictionary. Try something else.");
    else:
        bot.reply_to(message, "No query asked");
bot.polling()
