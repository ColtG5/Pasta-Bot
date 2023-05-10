import random
from variables import *

emilys_odds = random.randint(20, 30)

sydney_smells = ["stfu", "fuck", "shit", "i hate you", "hoe",
                  "kys", "kill your self", "kill yourself", "die",
                  "ass", "bitch"]
sydney_insults = ["Sydney kinda smells tbh", "Sydney u better stop w that shenanigans",
                   "RUDE SYDNEY!!!", "Rude! this y u a mistake ong", "Syd go wash ur mouth w that speak",
                   "u a damn shame with that attitude.", "sydney please speak nicely :pleading_face:"]
async def f_isItSydney(bot, message, channel, text, author):
    if (message.author.id == user_sydney_id):
        if any(word in text for word in sydney_smells):
            await message.channel.send(random.choice(sydney_insults))
        # if "tenor" in text:
        #     await message.delete()

async def f_isItColton(bot, message, channel, text, author):
    if (message.author.id == user_colton_id):
        # print("heyyy")
        if ("am i the bossman" in text) or ("am i the boss man" in text):
            await message.channel.send("Hell YEAH you are")

    # if message.author.id == user_colton_id:
    #     await message.delete()
async def f_isItAlex(bot, message, channel, text, author):
    if (message.author.id == user_alex_id):
        if "gabe" in text:
            await message.channel.send("(IM STEALING GABE FROM YOU) -Colton")

async def f_isItReese(bot, message, channel, text, author):
    if (message.author.id == user_reese_id):
        print("hehe stfu reese")
        # make code that deletes every message reese sends
        x = random.randint(1, 50)
        if (random.randint(1, 50) == 5):
            print(x)
            await message.delete()

async def f_isItBarwars(bot, message, channel, text, author):
    if (message.author.id == user_barwars_id):
        print("hehe stfu barwars")
        # if "tenor" in text:
        #     await message.delete()
        # make code that deletes every message barwars sends
        # if ():
        #     await message.delete()



async def f_isItEmily(bot, message, channel, text, author):
    global emilys_odds
    if (message.author.id == user_emily_id):
        pass
        # print("Emily odds: " + str(emilys_odds))
        # if emilys_odds > 1:
        #     emilys_odds -= 1
        # if random.randint(1, emilys_odds) == 1:
        #     current_nick = message.author.nick
        #     # message.author.edit(nick=current_nick[:-1])
        #     await message.author.edit(nick=current_nick[:-1])

# async def f_isItBjorn(bot, message, channel, text, author):
#     if (message.author.id == user_bjorn_id):
#         if random.randint(1, 200) == 1:
#             current_nick = message.author.nick
#             # message.author.edit(nick=current_nick[:-1])
#             await message.author.edit(nick=current_nick[:-1])

# async def f_isItAiden(bot, message, channel, text, author):
#     if (message.author.id == user_aiden_id):
#         if random.randint(1, 200) == 1:
#             current_nick = message.author.nick
#             # message.author.edit(nick=current_nick[:-1])
#             await message.author.edit(nick=current_nick[:-1])

# async def f_isItMason(bot, message, channel, text, author):
#     if (message.author.id == user_mason_id):
#         if random.randint(1, 200) == 1:
#             current_nick = message.author.nick
#             # message.author.edit(nick=current_nick[:-1])
#             await message.author.edit(nick=current_nick[:-1])

# async def f_isItGia(bot, message, channel, text, author):
#     if (message.author.id == user_gia_id):
#         if random.randint(1, 200) == 1:
#             current_nick = message.author.nick
#             # message.author.edit(nick=current_nick[:-1])
#             await message.author.edit(nick=current_nick[:-1])

async def f_isItStiters(bot, message, channel, text, author):
    if (message.author.id == user_stiters_id):
        print("hehe stfu stiters")
        # make code that deletes every message stiters sends
        # if (random.randint(1,10) == 1):
        await message.delete()