import os
import discord
from discord.ext import commands
from gtts import gTTS
from dotenv import load_dotenv

# get environment variables from .env file using library dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!pasta ", intents=intents)

@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))

@bot.event
async def on_message(message):
    author = message.author
    if author == bot.user:
        return
    
    if message.content.startswith("!pasta "): 
        # await message.channel.send("YE")
        await handle_user_request(message)
        
    await bot.process_commands(message)

async def handle_user_request(message):
    channel = message.channel
    user_request = message.content[7:].lower()

    import TextResponses
    for i in dir(TextResponses):
        function = getattr(TextResponses,i)
        if i.startswith('f_') and callable(function):
            await function(bot, message, channel, user_request)

if __name__ == '__main__':
    bot.run(os.environ.get('TOKEN'))