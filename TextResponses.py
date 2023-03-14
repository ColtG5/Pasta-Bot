import os
from Hangman import Hangman
from variables import *
import requests
import discord
from gtts import gTTS
import random
import yt_dlp
import json
import datetime
import asyncio

wait_time = 25
last_message_time = {}
greetings = ["hi", "hey", "hello"]
farewells = ["bye", "cya", "goodbye", "good bye"]
tishie = ["tishie", "dumb cat", "burger material", "bathtub shitter"]
misogyny = ["\"dishwasHER\" -ColtG5",
             "\"I’m not a misogynist, I respect any woman who knows her place.\" -Stephen Braithwaite",
             "\"The louder the woman, the more likely she is to be spiritually bereft, like an empty bowl which vibrates with a resonant echo. A full container makes no sound; she is packed too densely to ring.\" -Deborah Feldman",
             "\"Women upset everything. When you let them into your life, you find that the woman is driving at one thing and you’re driving at another.\" -George Bernard Shaw",
             "\"A proper wife should be as obedient as a slave . . . The female is a female by virtue of a certain lack of qualities . . . a natural defectiveness.\" -Aristotle",
             "\"Women are only stronger when they arm themselves with their weaknesses.\" -Marquise Du Deffand"]

async def f_pasta(bot, message, channel, req, upper_req):
    if req == "pasta":
        app_id = os.environ.get('FOOD_APP_ID')
        app_key = os.environ.get('FOOD_APP_KEY')
        query = "pasta"
        url = "https://api.edamam.com/search?q=" + query + "&app_id=" + app_id + "&app_key=" + app_key

        response = requests.get(url)
        print(response)

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

async def f_hello(bot, message, channel, req, upper_req):
    if req in greetings:
        user = message.author
        user = str(user).split("#")[0]
        await channel.send(f"Hello {user}!")

async def f_goodbye(bot, message, channel, req, upper_req):
    if req in farewells:
        user = message.author
        user = str(user).split("#")[0]
        if (user == "liltop"):
            await channel.send(f"no.")
        else:
            await channel.send(f"Goodbye {user}.")

async def f_thanks(bot, message, channel, req, upper_req):
    if req == "thanks":
        await channel.send("np")

async def f_fox(bot, message, channel, req, upper_req):
    if req == "fox":
        response = requests.get("https://randomfox.ca/floof/?ref=apilist.fun")
        image_link = response.json()["image"]
        await channel.send(image_link)

async def f_wisdom(bot, message, channel, req, upper_req):
    if req == "wisdom":
        response = requests.get("https://zenquotes.io/api/random").json()
        quote = "\"" + response[0]['q'] + "\"" + " -" + response[0]['a']
        await channel.send(quote)

async def f_misogyny(bot, message, channel, req, upper_req):
    if req == "misogyny":
        await channel.send(random.choice(misogyny))

async def f_tts(bot, message, channel, req, upper_req):
    if req.startswith("tts "):
        tts_text = req[4:]
        if "sydney" in tts_text.lower():
            tts_text = tts_text.replace("sydney", "dayvin")
        user = message.author
        # print(user.name)
        # print(user_emily_name)
        if user.voice is not None:
            if user.name == user_emily_name:
                # Check if the author has sent a message before
                print(last_message_time)
                if user.name in last_message_time:
                    last_time = last_message_time[user.name]
                    current_time = datetime.datetime.now()
                    time_elapsed = (current_time - last_time).total_seconds()
                    print(f"Time elapsed since last message: {time_elapsed} seconds")

                    if time_elapsed > wait_time:
                        await tts(bot, message, tts_text)
                    else:
                        await channel.send(f"{user.name}, you have to wait {wait_time} seconds between using tts! Cry to me about it! you have {round(wait_time - time_elapsed)} seconds left.")
                else:
                    await tts(bot, message, tts_text)
                # Store the time of the current message for the next comparison
                last_message_time[user.name] = datetime.datetime.now()
            else:
                await tts(bot, message, tts_text)
        else:
            await channel.send("Join vc to use this command!")

async def tts(bot, message, tts_text):
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

async def f_polar_bear(bot, message, channel, req, upper_req):
    if req == "polar bear":
        from animal_links import animals
        await channel.send("(Good choice)\n" + random.choice(animals.polar_bear_links_list))

async def f_mouse(bot, message, channel, req, upper_req):
    if req == "mouse" or req == "mice":
        from animal_links import animals
        await channel.send(random.choice(animals.mouse_links_list))

async def f_red_panda(bot, message, channel, req, upper_req):
    if req == "red panda":
        response = requests.get("https://some-random-api.ml/img/red_panda")
        image_link = response.json()["link"]
        await channel.send(image_link)

async def f_cat(bot, message, channel, req, upper_req):
    if req == "cat":
        response = requests.get("https://some-random-api.ml/img/cat")
        image_link = response.json()["link"]
        await channel.send(image_link)

async def f_dog(bot, message, channel, req, upper_req):
    if req == "dog":
        response = requests.get("https://some-random-api.ml/img/dog")
        image_link = response.json()["link"]
        await channel.send(image_link)

async def f_panda(bot, message, channel, req, upper_req):
    if req == "panda":
        response = requests.get("https://some-random-api.ml/img/panda")
        image_link = response.json()["link"]
        await channel.send(image_link)

async def f_koala(bot, message, channel, req, upper_req):
    if req == "koala":
        response = requests.get("https://some-random-api.ml/img/koala")
        image_link = response.json()["link"]
        await channel.send(image_link)

async def f_raccoon(bot, message, channel, req, upper_req):
    if req == "raccoon":
        response = requests.get("https://some-random-api.ml/img/raccoon")
        image_link = response.json()["link"]
        await channel.send(image_link)

async def f_milf(bot, message, channel, req, upper_req):
    if req == "milf":
        folder_path = "milfs"
        files = os.listdir(folder_path)
        image_files = [f for f in files if f.endswith((".png", ".jpg", ".jpeg", ".gif"))]

        random_file = random.choice(image_files)
        random_file_path = os.path.join(folder_path, random_file)

        with open(random_file_path, 'rb') as f:
            image = discord.File(f)
            await channel.send(file=image)

async def f_dilf(bot, message, channel, req, upper_req):
    if req == "dilf":
        folder_path = "dilfs"
        files = os.listdir(folder_path)
        image_files = [f for f in files if f.endswith((".png", ".jpg", ".jpeg", ".gif"))]

        random_file = random.choice(image_files)
        random_file_path = os.path.join(folder_path, random_file)

        with open(random_file_path, 'rb') as f:
            image = discord.File(f)
            await channel.send(file=image)

async def f_tishie(bot, message, channel, req, upper_req):
    if req in tishie:
        folder_path = "tishie"
        files = os.listdir(folder_path)
        image_files = [f for f in files if f.endswith((".png", ".jpg", ".jpeg", ".gif"))]

        random_file = random.choice(image_files)
        random_file_path = os.path.join(folder_path, random_file)

        with open(random_file_path, 'rb') as f:
            image = discord.File(f)
            await channel.send(file=image)

async def f_cheat_code(bot, message, channel, req, upper_req):
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

async def f_boobs(bot, message, channel, req, upper_req):
    if req == "boobs":
        user = message.author.name
        if user == user_emily_name:
            await channel.send("https://media.tenor.com/_ZvbLvrT_QcAAAAC/horny-jail-bonk.gif")

        elif user != user_colton_name:
            print(user)
            print(user_colton_name)
            x = random.randint(3,5)
            if x == 5:
                await get_tenor(channel)
            else:
                await channel.send("https://media.tenor.com/_ZvbLvrT_QcAAAAC/horny-jail-bonk.gif")
        else:
            await get_tenor(channel)

async def get_tenor(channel):
    apikey = "AIzaSyCiR3gYC7B1zsiROI1hz4Lx-5ObxMk-gkQ"
    limit = 50
    search_term = "boobs"
    r = requests.get(
        "https://tenor.googleapis.com/v2/search?q=%s&key=%s&limit=%s" % (search_term, apikey, limit))

    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        gifs = json.loads(r.content)
        x = random.randint(1, limit)
        gif = gifs['results'][x]['media_formats']['gif']['url']

        # Send the GIF to the channel
        await channel.send(gif)
    else:
        print("gif aint work")

async def f_join(bot, message, channel, req, upper_req):
    if req == "join":
        user = message.author
        if user.voice is None:
            await channel.send("get in a vc first ! ! !")
            return
        voice_client = discord.utils.get(bot.voice_clients, guild=message.guild)
        if voice_client and voice_client.is_connected():
            await channel.send("I'm already in a vc!")
            return
        voice_channel = message.author.voice.channel
        await voice_channel.connect()
        print(f"Connected to {voice_channel}")
        
async def f_play(bot, message, channel, req, upper_req):
    if req.startswith("play "):
        upper_req = upper_req[5:]
        if message.author.name == user_colton_name:
            if upper_req.startswith("https://www.youtube.com/"):
                user = message.author
                if user.voice is None:
                    await channel.send("get in a vc first")
                    return     
                voice_channel = message.author.voice.channel
                voice_client = discord.utils.get(bot.voice_clients, guild=message.guild)
                if (voice_client is not None) and (voice_client.channel != voice_channel):
                    print("in a diff vc")
                    await voice_client.disconnect()
                    voice_client = None
                if voice_client is None:
                    print("in no vc")
                    voice_client = await voice_channel.connect()

                ydl_opts = {
                    'format': 'bestaudio/best',       
                    'outtmpl': 'youtube-audio.mp3',       
                    'noplaylist' : True,   
                    'nooverwrites': False,        
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([upper_req])
                
                source = discord.FFmpegOpusAudio(executable="C:\\Program Files\\ffmpeg\\ffmpeg-6.0-full_build\\bin\\ffmpeg.exe", source="youtube-audio.mp3", options="-b:a 64k")
                voice_client.play(source)
            else:
                await channel.send("bruh")
        else:
            await channel.send("chump")

async def f_stop(bot, message, channel, req, upper_req):
    if req == "stop":
        voice_client = discord.utils.get(bot.voice_clients, guild=message.guild)
        if voice_client and voice_client.is_playing():
            voice_client.stop()
            print(f"Stopped {voice_client.channel}")
        else:
            print("get in a vc")

async def f_leave(bot, message, channel, req, upper_req):
    if req == "leave":
        voice_client = discord.utils.get(bot.voice_clients, guild=message.guild)
        if voice_client and voice_client.is_connected():
            await voice_client.disconnect()
            print(f"Disconnected from {voice_client.channel}")
        else:
            print("I was told to leave voice channel, but was not in one")  

async def f_dc(bot, message, channel, req, upper_req):
    if req == "dc":
        voice_client = discord.utils.get(bot.voice_clients, guild=message.guild)
        if voice_client and voice_client.is_connected():
            await voice_client.disconnect()

async def f_pun(bot, message, channel, req, upper_req):
    if req == "pun":
        headers = {
        "Accept": "application/json"
        }
        pun = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
        print(pun)
        await channel.send(pun["joke"])

shiny_messages = ["damn, you got a shiny!", "SHINYYYYYYYYYYYY", "That's a shiny, well done!"]
shiny_messages_parker = ["Parker the absolute goat with yet another shiny somehow", "Now this is a Parker moment", "Nice shiny Parker!"]
shiny_odds = 673

async def f_pokemon(bot, message, channel, req, upper_req):
    if req.startswith("pokemon"):
        count = requests.get(f"https://pokeapi.co/api/v2/pokemon/?limit=1&offset=1").json().get("count")
        x = random.randint(1, count)
        # print(count)
        pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/?limit=1&offset={x}").json()
        poke = pokemon.get("results")[0].get("url")
        shiny_chance = random.randint(1, shiny_odds)
        if req[8:] == "shiny":
            if user_colton_name != message.author.name:
                await channel.send("you're not him :rofl:")
                return
            else:
                pic = requests.get(poke).json().get("sprites").get("other").get("official-artwork").get("front_shiny")
                await channel.send(pic)
                await channel.send(random.choice(shiny_messages))
                return

        if shiny_chance == 5:
            pic = requests.get(poke).json().get("sprites").get("other").get("official-artwork").get("front_shiny")
            if message.author.name == user_parker_name:
                await channel.send(pic)
                await channel.send(random.choice(shiny_messages_parker))
            else:
                await channel.send(pic)
                await channel.send(random.choice(shiny_messages))
        else:
            pic = requests.get(poke).json().get("sprites").get("other").get("official-artwork").get("front_default")
            await channel.send(pic)

async def f_sydney_based(bot, message, channel, req, upper_req):
    if req == "sydney based":
        if message.author.name == user_sydney_name:
            folder_path = "pics"
            files = os.listdir(folder_path)
            image_files = [f for f in files if f.endswith((".png", ".jpg", ".jpeg", ".gif"))]

            random_file = random.choice(image_files)
            random_file_path = os.path.join(folder_path, random_file)

            with open(random_file_path, 'rb') as f:
                image = discord.File(f)
                await channel.send(file=image)
        else:
            await channel.send("you're not the disney princess herself unfortunately")

eight_ball_responses = ["It is certain", "Don’t count on it", 
                        "It is decidedly so", "My reply is no", 
                        "Without a doubt", "Better not tell you now", "My sources say no", 
                        "Yes definitely", "Outlook not so good", 
                        "You may rely on it", "Concentrate and ask again", "Very doubtful",
                        "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes"]

async def f_8ball(bot, message, channel, req, upper_req):
    if req.startswith("8ball "):
        if not req.endswith("?"):
            await channel.send("Ask the 8 ball a question! (end with a '?')")
        else:
            await channel.send(random.choice(eight_ball_responses))

hangman_games = {}

async def f_hangman(bot, message, channel, req, upper_req):
    author = message.author
    if req == "hangman":
        await channel.send("Pasta hangman!\nHangman commands: \nstart \nend \n<letter>")
        return
    if req.startswith("hangman "):
        req = req[8:]
        if req == "start":
            if author in hangman_games:
                await channel.send("You're already in a game!")
                return
            else:
                hangman_game = Hangman(author, Hangman.choose_random_word())
                hangman_games[author] = hangman_game
                await channel.send(hangman_game.start_up())
                return
        if req == "end":
            if author not in hangman_games:
                await channel.send("You don't have a game to end!")
                return
            else:
                hangman_game = hangman_games[author]
                await channel.send(hangman_game.end())
                del hangman_games[author]
                return

        if len(req) == 1 and req.isalpha():
            if author in hangman_games:
                hangman_game = hangman_games[author]
                await channel.send(hangman_game.guess(req))
                if hangman_game.done:
                    del hangman_games[author]
                return
            else:
                await channel.send("Start a game before guessing a letter!")
                return
        await channel.send("Invalid hangman command! type 'hangman' for help")
        
acceptable_apologies = ["Colton is the bestest ever! I just love everything about him. He definitely deserves the world!"]

async def f_emily(bot, message, channel, req, upper_req):
    print("here3")
    if req.startswith("emily"):
        print("here2")
        req = upper_req[6:]
        if (message.author.name == user_emily_name) or message.author.name == user_colton_name:
            print("here")
            print(req)
            if req in acceptable_apologies:
                import AuthorSendsMessage
                emilys_odds = AuthorSendsMessage.emilys_odds
                await channel.send(f"Thank you!. Odds have been changed from 1 in {emilys_odds} to 1 in {emilys_odds + 50}.")
                emilys_odds += 50
                AuthorSendsMessage.emilys_odds = emilys_odds
            else:
                await channel.send(f"That's not a valid request Ms. Lane. (hint: try `{acceptable_apologies[0]}`)")
        else:
            await channel.send("You're not emily, you can't change her odds for her.")
