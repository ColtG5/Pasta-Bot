import random
from variables import *

sydney_smells = ["stfu", "shut up", "rude", "hey", "fuck", "shit", "i hate you", "stop", "kys", "kill your self", "kill yourself", "die", "dumb", "stupid"]
sydney_insults = ["Sydney kinda smells tbh", "Sydney u better stop w that shenanigans", "RUDE SYDNEY!!!", "Rude! this y u a mistake ong", "Syd go ash ur mouth w that speak"]
async def f_isItSydney(bot, message, channel, text, author):
    if (author == "Sydney"):
        if any(word in text for word in sydney_smells):
            await message.channel.send(random.choice(sydney_insults))

async def f_isItColton(bot, message, channel, text, author):
    if (author == "ColtG5"):
        if ("am i the bossman" in text) or ("am i the boss man" in text):
            await message.channel.send("Hell YEAH you are")

async def f_isItAlex(bot, message, channel, text, author):
    if (author == "Astrellex"):
        if "gabe" in text:
            await message.channel.send("(IM STEALING GABE FROM YOU) -Colton")