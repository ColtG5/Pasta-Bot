import random
from variables import *

emilys_odds = random.randint(20, 30)

sydney_smells = ["stfu", "shut up", "rude", "fuck", "shit", "i hate you", "hoe",
                  "stop", "kys", "kill your self", "kill yourself", "die", "dumb", "stupid"
                  "ass", "bitch"]
sydney_insults = ["Sydney kinda smells tbh", "Sydney u better stop w that shenanigans",
                   "RUDE SYDNEY!!!", "Rude! this y u a mistake ong", "Syd go wash ur mouth w that speak",
                   "u a damn shame with that attitude.", "sydney please speak nicely :pleading_face:"]
async def f_isItSydney(bot, message, channel, text, author):
    if (author == user_sydney_name):
        if any(word in text for word in sydney_smells):
            await message.channel.send(random.choice(sydney_insults))

async def f_isItColton(bot, message, channel, text, author):
    if (author == user_colton_name):
        if ("am i the bossman" in text) or ("am i the boss man" in text):
            await message.channel.send("Hell YEAH you are")
async def f_isItAlex(bot, message, channel, text, author):
    if (author == user_alex_name):
        if "gabe" in text:
            await message.channel.send("(IM STEALING GABE FROM YOU) -Colton")

async def f_isItEmily(bot, message, channel, text, author):
    global emilys_odds
    if (author == user_emily_name):
        pass
        # print("Emily odds: " + str(emilys_odds))
        # if emilys_odds > 1:
        #     emilys_odds -= 1
        # if random.randint(1, emilys_odds) == 1:
        #     current_nick = message.author.nick
        #     # message.author.edit(nick=current_nick[:-1])
        #     await message.author.edit(nick=current_nick[:-1])

async def f_isItBjorn(bot, message, channel, text, author):
    if (author == user_bjorn_name):
        if random.randint(1, 200) == 1:
            current_nick = message.author.nick
            # message.author.edit(nick=current_nick[:-1])
            await message.author.edit(nick=current_nick[:-1])

async def f_isItAiden(bot, message, channel, text, author):
    if (author == user_aiden_name):
        if random.randint(1, 200) == 1:
            current_nick = message.author.nick
            # message.author.edit(nick=current_nick[:-1])
            await message.author.edit(nick=current_nick[:-1])

async def f_isItMason(bot, message, channel, text, author):
    if (author == user_mason_name):
        if random.randint(1, 200) == 1:
            current_nick = message.author.nick
            # message.author.edit(nick=current_nick[:-1])
            await message.author.edit(nick=current_nick[:-1])

async def f_isItGia(bot, message, channel, text, author):
    if (author == user_gia_name):
        if random.randint(1, 200) == 1:
            current_nick = message.author.nick
            # message.author.edit(nick=current_nick[:-1])
            await message.author.edit(nick=current_nick[:-1])