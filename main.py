import os
from variables import *
import random
import asyncio
import datetime
import discord
from discord.ext import commands
from gtts import gTTS
from dotenv import load_dotenv
import TextResponses


# get environment variables from .env file using library dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!pasta ", intents=intents)
bot.remove_command('help')

chump_lounge = None

@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))
    bot.loop.create_task(send_daily_polar_bear())
    bot.loop.create_task(send_daily_emi_meds_reminder())

    chump_lounge = bot.get_guild(905206514665529445) # chump lounge
    # pUHsta = bot.get_guild(1081413943853060137) # pUHsta
    emi = await chump_lounge.fetch_member(user_emi_id)
    # colton = await chump_lounge.fetch_member(user_colton_id)
    global emi_string
    emi_string = f"{emi.mention}, it's time to take your meds emi!"
    # global colton_string
    # colton_string = f"{colton.mention}, it's time to take your meds emi!"

    for guild in bot.guilds:
        if guild.me.guild_permissions.view_audit_log:
            print(f"{bot.user} has permission to view audit logs in {guild}")
        else:
            print(f"{bot.user} does not have permission to view audit logs in {guild}")

@bot.event
async def on_message(message):
    # print(message.guild)
    author = message.author
    text = message.content.lower()
    if author == bot.user:
        return
    
    if text.startswith("!pasta "): 
        await handle_user_request(message)
    else:
        # await handle_keyword(message)
        pass
    await handle_author(message)

    await bot.process_commands(message)

async def handle_user_request(message):
    channel = message.channel
    normal_req = message.content[7:]
    user_request = message.content[7:].lower()
    # req_text = message.content

    import TextResponses
    for i in dir(TextResponses):
        function = getattr(TextResponses,i)
        if i.startswith('f_') and callable(function):
            await function(bot, message, channel, user_request, normal_req)
    
async def handle_author(message):
    channel = message.channel
    text = message.content.lower()
    author = message.author.name

    import AuthorSendsMessage
    for i in dir(AuthorSendsMessage):
        function = getattr(AuthorSendsMessage,i)
        if i.startswith('f_') and callable(function):
            await function(bot, message, channel, text, author)

@bot.command(name="help")
async def bot_commands(ctx):
    bot_functions = []
    import TextResponses
    for i in dir(TextResponses):
        function = getattr(TextResponses,i)
        if i.startswith('f_') and callable(function):
            bot_functions.append(i[2:])

    bot_functions = [i.replace("_", " ") for i in bot_functions]
    bot_functions[bot_functions.index("tts")] = "tts [message] (have to be in a vc)"
    bot_functions[bot_functions.index("pokemon")] = "pokemon (1/673 chance for a shiny!)"
    bot_functions[bot_functions.index("sydney based")] = "sydney based (sydney exclusive!)"
    bot_functions[bot_functions.index("8ball")] = "8ball [question] ?"
    bot_functions[bot_functions.index("my ass ta")] = "my-ass-ta"

    intro = "```Pasta Bot!\nUsage: !pasta <command> [arguments (for some)] | Current commands:\n"
    funcs = "\n".join(bot_functions)
    await ctx.send(intro + "\n" + funcs + "```")

polar_bear_pic_mesages = ["Here is your polar bear picture for the day:", "Enjoy this lovely polar bear picture to start your day off:",
                          "Here is a polar bear picture to brighten your day:", "Here is a polar bear picture to make your day better:",
                          "Polar bear SUPERMACY BABY", "Daily polar bear picture, as promised:"]

async def send_daily_polar_bear():
    await bot.wait_until_ready()
    channels = [799154480947134491, 966107743213748274, 905206514665529448, 1081413945329463339]
    channels1 = [1081413945329463339]
    while not bot.is_closed():
        now = datetime.datetime.now().time()
        send_time = datetime.time(hour=8, minute=0, second=0)
        buffer_time = datetime.time(hour=8, minute=0, second=5)
        # If it's the send time, send the message
        if buffer_time >= now >= send_time:
            from animal_links import animals
            print(now)
            print(send_time)
            for channel_num in channels:
                # print(type(channel_num))
                channel = bot.get_channel(channel_num)
                # print(type(channel))
                await channel.send(random.choice(polar_bear_pic_mesages))
                await channel.send(random.choice(animals.polar_bear_links_list))
            # Wait until the next day to send the message again
            tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
            send_time = datetime.datetime.combine(tomorrow.date(), send_time)
            wait_time = (send_time - datetime.datetime.now()).total_seconds()
            await asyncio.sleep(wait_time)
        else:
            # Wait until the send time
            wait_time = (datetime.datetime.combine(datetime.date.today(), send_time) - datetime.datetime.now()).total_seconds()
            if wait_time < 0:
                wait_time += 86400
            print(wait_time)
            await asyncio.sleep(wait_time)
            print("errerere")


waiting_for_emis_response = False
emi_string = None
colton_string = None
med_counter = 0
emi_small_wait_time = 300
async def send_daily_emi_meds_reminder():
    global waiting_for_emis_response
    # global colton_string
    global emi_string
    global med_counter
    global emi_small_wait_time
    await bot.wait_until_ready()
    channel = bot.get_channel(1086882547973230714)
    # channel = bot.get_channel(1081413945329463339) # pUHsta
    while not bot.is_closed():
        now = datetime.datetime.now().time()
        # send_time = datetime.time(hour=21, minute=30, second=0)
        # buffer_time = datetime.time(hour=21, minute=30, second=5)
        send_time = datetime.time(hour=21, minute=30, second=0)
        TextResponses.woohoo = send_time
        # emi_send_time = send_time
        # set_emi_send_time(send_time)
        # print(f"udapted to {emi_send_time}")
        buffer_time = datetime.time(hour=21, minute=30, second=5)
        # buffer_time = send_time + datetime.timedelta(seconds=5)
        # If it's the send time, send the message
        
        if (not waiting_for_emis_response):
            if buffer_time >= now >= send_time:
                await channel.send(emi_string)
                # await channel.send(colton_string)
                print("reminded emi about her meds") 
                med_counter += 1
                # Wait until the next day to send the message again
                tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
                send_time = datetime.datetime.combine(tomorrow.date(), send_time)
                TextResponses.woohoo = send_time

                # emi_wait_time = (send_time - datetime.datetime.now()).total_seconds()
                waiting_for_emis_response = True
                TextResponses.waiting_for_emi = True
                await asyncio.sleep(emi_small_wait_time)
            else:
                # Wait until the send time
                # emi_send_time = send_time
                # print(f"set emi_send_time to {emi_send_time}")
                wait_time = (datetime.datetime.combine(datetime.date.today(), send_time) - datetime.datetime.now()).total_seconds()
                if wait_time < 0:
                    wait_time += 86400
                await asyncio.sleep(wait_time)
        else:
            if TextResponses.emi_responded == True:
                waiting_for_emis_response = False;
                TextResponses.emi_responded = False;
                TextResponses.waiting_for_emi = False;
                med_counter = 0
                # emi_send_time = send_time
                wait_time = (datetime.datetime.combine(datetime.date.today(), send_time) - datetime.datetime.now()).total_seconds()
                if wait_time < 0:
                    wait_time += 86400
                await asyncio.sleep(wait_time)

            else:
                # i_stg_emi = "!" * (med_counter * 3)
                i_stg_emi = "!" * (2 ** med_counter)
                if (len(i_stg_emi) > 1900):
                    i_stg_emi = "!" * 1900
                await channel.send(emi_string + f"{i_stg_emi}")
                med_counter += 1
                print("reminded emi about her meds" + f" ({med_counter} times)")
                await asyncio.sleep(emi_small_wait_time)

@bot.event
async def on_voice_state_update(member, before, after):
    if member.bot and after.channel is None:
        async for entry in before.channel.guild.audit_logs(limit=1, action=discord.AuditLogAction.member_disconnect):
            if entry.user.name == user_bjorn_name:
                # print(entry.user.name, user_colton_name)
                print(f"{member} was disconnected from {before.channel} by {entry.user}")
                await entry.user.edit(mute=True)

@bot.event
async def on_member_update(before, after):
    if after.id == bot.user.id:  # Check if the updated member is the bot
        if before.nick != after.nick:  # Check if the nickname has changed
            print(f"The bot's nickname was changed from {before.nick} to {after.nick} by {after.display_name}")

if __name__ == '__main__':
    bot.run(os.environ.get('TOKEN'))