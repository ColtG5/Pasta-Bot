import os
from variables import *
import requests
import discord
from gtts import gTTS
import random
import yt_dlp

greetings = ["hi", "hey", "hello"]
farewells = ["bye", "cya", "goodbye", "good bye"]
tishie = ["tishie", "dumb cat", "burger material", "bathtub shitter"]
misogyny = ["\"dishwasHER\" -ColtG5",
             "\"I’m not a misogynist, I respect any woman who knows her place.\" -Stephen Braithwaite",
             "\"The louder the woman, the more likely she is to be spiritually bereft, like an empty bowl which vibrates with a resonant echo. A full container makes no sound; she is packed too densely to ring.\" -Deborah Feldman",
             "\"Women upset everything. When you let them into your life, you find that the woman is driving at one thing and you’re driving at another.\" -George Bernard Shaw",
             "\"A proper wife should be as obedient as a slave . . . The female is a female by virtue of a certain lack of qualities . . . a natural defectiveness.\" -Aristotle",
             "\"Women are only stronger when they arm themselves with their weaknesses.\" -Marquise Du Deffand"]

async def f_pasta(bot, message, channel, req):
    if req == "pasta":
        app_id = os.environ.get('APP_ID')
        app_key = os.environ.get('APP_KEY')
        query = "pasta"
        url = f"https://api.edamam.com/search?q={query}&app_id={app_id}&app_key={app_key}"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            hits = data["hits"]
            if len(hits) > 0:
                rand = random.randint(0, len(hits) - 1)
                hit = hits[rand]["recipe"]
                image_url = hit["image"]
                await channel.send(image_url)
        else:
            print("Error: could not retrieve data from API.")

async def f_hello(bot, message, channel, req):
    if req in greetings:
        user = message.author
        user = str(user).split("#")[0]
        await channel.send(f"Hello {user}!")

async def f_goodbye(bot, message, channel, req):
    if req in farewells:
        user = message.author
        user = str(user).split("#")[0]
        if (user == "liltop"):
            await channel.send(f"no.")
        else:
            await channel.send(f"Goodbye {user}.")

async def f_thanks(bot, message, channel, req):
    if req == "thanks":
        await channel.send("np")

async def f_fox(bot, message, channel, req):
    if req == "fox":
        response = requests.get("https://randomfox.ca/floof/?ref=apilist.fun")
        image_link = response.json()["image"]
        await channel.send(image_link)

async def f_wisdom(bot, message, channel, req):
    if req == "wisdom":
        response = requests.get("https://zenquotes.io/api/random").json()
        quote = "\"" + response[0]['q'] + "\"" + " -" + response[0]['a']
        await channel.send(quote)

async def f_misogyny(bot, message, channel, req):
    if req == "misogyny":
        await channel.send(random.choice(misogyny))

async def f_tts(bot, message, channel, req):
    if req.startswith("tts "):
        tts_text = req[4:]
        user = message.author
        if user.voice is not None:
            voice_channel = message.author.voice.channel
            voice_client = discord.utils.get(bot.voice_clients, guild=message.guild)
            if (voice_client is not None) and (voice_client.channel != voice_channel):
                await voice_client.disconnect()
                voice_client = None
            if voice_client is None:
                voice_client = await voice_channel.connect()

            sound = gTTS(text=tts_text, lang="en", slow=False)
            sound.save("tts-audio.mp3")

            if voice_client.is_playing():
                voice_client.stop()

            source = discord.FFmpegOpusAudio(executable="C:\\Program Files\\ffmpeg\\ffmpeg-6.0-full_build\\bin\\ffmpeg.exe", source="tts-audio.mp3")
            if voice_client is None or not voice_client.is_connected():
                return
            try:
                voice_client.play(source)
            except Exception as e:
                print(e)
                return
        else:
            await channel.send("Join vc to use this command!")

async def f_polar_bear(bot, message, channel, req):
    if req == "polar bear":
        from polar_bears import polar_bear_links
        await channel.send("(Good choice)\n" + random.choice(polar_bear_links.polar_bear_links_list))

async def f_red_panda(bot, message, channel, req):
    if req == "red panda":
        response = requests.get("https://some-random-api.ml/img/red_panda")
        image_link = response.json()["link"]
        await channel.send(image_link)

async def f_cat(bot, message, channel, req):
    if req == "cat":
        response = requests.get("https://some-random-api.ml/img/cat")
        image_link = response.json()["link"]
        await channel.send(image_link)

async def f_dog(bot, message, channel, req):
    if req == "dog":
        response = requests.get("https://some-random-api.ml/img/dog")
        image_link = response.json()["link"]
        await channel.send(image_link)

async def f_panda(bot, message, channel, req):
    if req == "panda":
        response = requests.get("https://some-random-api.ml/img/panda")
        image_link = response.json()["link"]
        await channel.send(image_link)

async def f_koala(bot, message, channel, req):
    if req == "koala":
        response = requests.get("https://some-random-api.ml/img/koala")
        image_link = response.json()["link"]
        await channel.send(image_link)

async def f_raccoon(bot, message, channel, req):
    if req == "raccoon":
        response = requests.get("https://some-random-api.ml/img/raccoon")
        image_link = response.json()["link"]
        await channel.send(image_link)

async def f_milf(bot, message, channel, req):
    if req == "milf":
        folder_path = "milfs"
        files = os.listdir(folder_path)
        image_files = [f for f in files if f.endswith((".png", ".jpg", ".jpeg", ".gif"))]

        random_file = random.choice(image_files)
        random_file_path = os.path.join(folder_path, random_file)

        with open(random_file_path, 'rb') as f:
            image = discord.File(f)
            await channel.send(file=image)

async def f_dilf(bot, message, channel, req):
    if req == "dilf":
        folder_path = "dilfs"
        files = os.listdir(folder_path)
        image_files = [f for f in files if f.endswith((".png", ".jpg", ".jpeg", ".gif"))]

        random_file = random.choice(image_files)
        random_file_path = os.path.join(folder_path, random_file)

        with open(random_file_path, 'rb') as f:
            image = discord.File(f)
            await channel.send(file=image)

async def f_tishie(bot, message, channel, req):
    if req in tishie:
        folder_path = "tishie"
        files = os.listdir(folder_path)
        image_files = [f for f in files if f.endswith((".png", ".jpg", ".jpeg", ".gif"))]

        random_file = random.choice(image_files)
        random_file_path = os.path.join(folder_path, random_file)

        with open(random_file_path, 'rb') as f:
            image = discord.File(f)
            await channel.send(file=image)

async def f_cheat_code(bot, message, channel, req):
    if req == "cheat code":
        arrow_up = discord.PartialEmoji(name=':arrow_up:', id=None).__str__()
        arrow_down = discord.PartialEmoji(name=':arrow_down:', id=None).__str__()
        arrow_left = discord.PartialEmoji(name=':arrow_left:', id=None).__str__()
        arrow_right = discord.PartialEmoji(name=':arrow_right:', id=None).__str__()
        b = discord.PartialEmoji(name=':regional_indicator_b:', id=None).__str__()
        a = discord.PartialEmoji(name=':regional_indicator_a:', id=None).__str__()
        start = discord.PartialEmoji(name=':arrow_forward:', id=None).__str__()
        # await message.channel.send(arrow_up + arrow_up + arrow_down + arrow_down + arrow_left + arrow_right + arrow_left + arrow_right + b + a + start)
        # join objects into a string
        await message.channel.send("".join([arrow_up, arrow_up, arrow_down, arrow_down, arrow_left, arrow_right, arrow_left, arrow_right, b, a, start]))

async def f_boobs(bot, message, channel, req):
    if req == "boobs":
        await channel.send("https://media.tenor.com/_ZvbLvrT_QcAAAAC/horny-jail-bonk.gif")

async def f_join(bot, message, channel, req):
    if req == "join":
        user = message.author
        if user.voice is None:
            await channel.send("get in a vc first")
            return
        voice_client = discord.utils.get(bot.voice_clients, guild=message.guild)
        if voice_client and voice_client.is_connected():
            await channel.send("I'm already in a vc!")
            return
        voice_channel = message.author.voice.channel
        await voice_channel.connect()
        print(f"Connected to {voice_channel}")
        
async def f_play(bot, message, channel, req):
    if req.startswith("play "):
        to_play = req[5:]
        user = message.author
        if user.voice is None:
            await channel.send("get in a vc first")
            return     
        voice_channel = message.author.voice.channel
        voice_client = discord.utils.get(bot.voice_clients, guild=message.guild)
        print("here")
        if (voice_client is not None) and (voice_client.channel != voice_channel):
            print("in a diff vc")
            await voice_client.disconnect()
            voice_client = None
        if voice_client is None:
            print("in no vc")
            voice_client = await voice_channel.connect()

                # Use yt-dlp to extract info about the YouTube video
        # with yt_dlp.YoutubeDL({'outtmpl': 'video.mp4'}) as ydl:
        #     info = ydl.extract_info(to_play, download=True)
        #     filename = ydl.prepare_filename(info)
        #     source = discord.FFmpegPCMAudio(filename)
        #     voice_client.play(source)

        ydl_opts = {
            'format': 'bestaudio/best',       
            'outtmpl': 'youtube-audio.mp3',       
            'noplaylist' : True,   
            'nooverwrites': False,        
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(['https://www.youtube.com/watch?v=8CWy_-afIpY&ab_channel=TheWeeknd-Topic'])
        
        source = discord.FFmpegOpusAudio(executable="C:\\Program Files\\ffmpeg\\ffmpeg-6.0-full_build\\bin\\ffmpeg.exe", source="youtube-audio.mp3", options="-b:a 64k")
        voice_client.play(source)

async def f_leave(bot, message, channel, req):
    if req == "leave":
        voice_client = discord.utils.get(bot.voice_clients, guild=message.guild)
        if voice_client and voice_client.is_connected():
            await voice_client.disconnect()
            print(f"Disconnected from {voice_client.channel}")
        else:
            print("I was told to leave voice channel, but was not in one")  

async def f_pun(bot, message, channel, req):
    if req == "pun":
        headers = {
        "Accept": "application/json"
        }
        pun = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
        print(pun)
        await channel.send(pun["joke"])