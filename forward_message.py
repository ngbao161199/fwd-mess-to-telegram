import logging
#import MetaTrader5 as mt5
import time
from telegram.ext import Updater, MessageHandler, Filters

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Initialize MetaTrader 5
#mt5.initialize()

# Source channel ID
source_channel_id = # your source channel id
destination_channel_id = # your destination channel id

# Define a function to handle incoming messages (THIS BOT TEST FOR AUDCAD & XAUUSD only
def forward_message(update, context):
    message = update.effective_message
    #order = message.text
    #chat_id = message.chat_id

    if message.text and "PAIR: AUDCAD" in message.text and "SIDE: sell" in message.text:  # AUDCAD sell
        #positions = mt5.positions_get()
        context.bot.send_message(chat_id=destination_channel_id, text="RFC CLOSE AUDCAD")
        time.sleep(2)
        context.bot.send_message(chat_id=destination_channel_id, text="sell AUDCAD")

        #context.bot.send_message(chat_id=update.effective_chat.id, text="RFC CLOSE AUDCAD")
        #time.sleep(2)
        #context.bot.send_message(chat_id=update.effective_chat.id, text="sell AUDCAD")

    if message.text and "PAIR: AUDCAD" in message.text and "SIDE: buy" in message.text:  # AUDCAD buy
        context.bot.send_message(chat_id=destination_channel_id, text="RFC CLOSE AUDCAD")
        time.sleep(2)
        context.bot.send_message(chat_id=destination_channel_id, text="buy AUDCAD")

    if message.text and "PAIR: XAUUSD" in message.text and "SIDE: buy" in message.text:  # XAUUSD buy
        context.bot.send_message(chat_id=destination_channel_id, text="RFC CLOSE XAUUSD")
        time.sleep(2)
        context.bot.send_message(chat_id=destination_channel_id, text="buy XAUUSD")

    if message.text and "PAIR: XAUUSD" in message.text and "SIDE: sell" in message.text:  # XAUUSD sell
        context.bot.send_message(chat_id=destination_channel_id, text="RFC CLOSE XAUUSD")
        time.sleep(2)
        context.bot.send_message(chat_id=destination_channel_id, text="sell XAUUSD")

        #message = update.effective_message
        #if message.text and "Close all AUDCAD success" in message.text:
        #
        #    context.bot.send_message(chat_id=update.effective_chat.id, text=other)
        #    pass
        #if message.text and "XAUUSD" in message.text:  # XAUUSD
        #    context.bot.send_message(chat_id=update.effective_chat.id, text="RFC CLOSE XAUUSD")
        #    context.bot.send_message(chat_id=update.effective_chat.id, text=other)


# Create an instance of the Updater and pass in your bot's API token
updater = Updater(token='YOUR BOT API TOKEN HERE', use_context=True)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# Register the handle_message function to handle incoming messages
message_handler = MessageHandler(Filters.chat(chat_id=source_channel_id), forward_message)
dispatcher.add_handler(message_handler)

# Start the bot
updater.start_polling()
