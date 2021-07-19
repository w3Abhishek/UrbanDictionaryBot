import json
import requests
import telebot

# Enter Your Bot Token in place of TOKEN
bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=["ud"])  # /ud command will invoke this function
def send_welcome(message):
    # Picking the requested word from Telegram message
    search_term = message.text[4:]

    if search_term:  # Condition ensures that some query is passed with command /ud
        # Passing Query to Urban Dictionary API
        api_response = requests.get(
            "http://api.urbandictionary.com/v0/define?term=" + search_term
        )
        ud_response = json.loads(
            api_response.text
        )  # Loads the json response in Text format and then passes to ud_response variable

        if ud_response["list"]:  # Check whether response is empty or not
            bot_response = (
                str("Meaning of " + search_term)
                + str("\n\n" + ud_response["list"][0]["definition"])
                + str("\n\nExample: " + ud_response["list"][0]["example"])
            )
            bot.reply_to(message, bot_response)
        else:
            bot.reply_to(
                message, "No meaning available on Urban Dictionary. Try something else."
            )
    else:
        bot.reply_to(message, "No query asked")


bot.polling()
