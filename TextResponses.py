import os
import requests
import discord
from gtts import gTTS
import random

greetings = ["hi", "hey", "hello"]
farewells = ["bye", "cya", "goodbye", "good bye"]
tishie = ["tishie", "dumb cat", "burger material", "bathtub shitter"]

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

async def f_tts(bot, message, channel, req): 
    if req.startswith("tts "):
        tts_text = req[4:]
        user = message.author
        if user.voice != None:
            voice_channel = message.author.voice.channel
            # print("Voice channel: " + str(voice_channel))
            # print()
            # print(bot.voice_clients)
            # print()
            voice_client = discord.utils.get(bot.voice_clients, guild=message.guild)
            # print(voice_client)
            if (voice_client != None) and (voice_client.channel != voice_channel):
                await voice_client.disconnect()
                voice_client = None
            if voice_client == None:
                voice_client = await voice_channel.connect()

            # print(voice_client)
            
            sound = gTTS(text=tts_text, lang="en", slow=False)
            sound.save("tts-audio.mp3")
    
            if voice_client.is_playing():
                voice_client.stop()
    
            source = discord.FFmpegOpusAudio(executable="C:\\Program Files\\ffmpeg\\ffmpeg-6.0-full_build\\bin\\ffmpeg.exe", source="tts-audio.mp3")
            voice_client.play(source)
        else:
            await channel.send("Join vc to use this command!")

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


        