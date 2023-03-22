import aiogram
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = aiogram.Bot(token='API_KEY')
dsp = Dispatcher(bot)

# Define a function to handle messages
@dsp.message_handler()
async def handle_message(message: types.Message):
    # Get the text of the message
    text = message.text.lower()
    
    # Check if the message is a command
    if text.startswith('/'):
        # If it is a command, handle it
        if text == '/start':
            await message.reply("Hello, I am a Telegram bot! I can do the following:\n\n"
                               "/start - Show this message\n"
                               "/help - Show a list of commands\n"
                               "/echo - Repeat a message\n")

        elif text == '/help':
            await message.reply("I can do the following:\n\n"
                               "/start - Show a list of commands\n"
                               "/help - Show this message\n"
                               "/echo - Repeat a message\n")

        elif text.startswith('/echo'):
            # Get the text to repeat
            repeat = text[6:]
            
            # Check if there is any text
            if repeat:
                # If there is text, repeat it
                await message.reply(repeat)
            else:
                # If there is no text, show an error message
                await message.reply("Error: No message to repeat")
        
        else:
            # If the command is not recognized, show an error message
            await message.reply("Error: Unrecognized command")

    elif 'hello' in text or 'hi' in text:
        await message.reply("Hello, I am a Telegram bot! I can do the following:\n\n"
                            "/start - Show this message\n"
                            "/help - Show a list of commands\n"
                            "/echo - Repeat a message\n")
    
    elif 'who are you' in text:
        await message.reply("I am a Telegram bot!, how can I help you")

    else:
        # If the message is not a command, show a default response
        await message.reply("I'm sorry, I don't know how to respond to that")

# Start the bot and listen for updates
executor.start_polling(dsp)
