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
import main

woohoo = 0
pasta_volume = 0.02
emi_responded = False
waiting_for_emi = False
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
        if (random.randint(1,100) == 5):
            dd_file_path = ".\dilfs\secret-danny-photo\IMG_3664.jpg"
            with open(dd_file_path, 'rb') as f:
                image = discord.File(f)
                await channel.send(message.author.mention + " You got the RARE Danny DeVito photo :eyes::eyes::eyes:")
                await channel.send(file=image)
        else:
            folder_path = "dilfs"
            files = os.listdir(folder_path)
            image_files = [f for f in files if f.endswith((".png", ".jpg", ".jpeg", ".gif", "jpg_large"))]

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
            # print(user)
            # print(user_colton_name)
            x = random.randint(3,5)
            if x == 5:
                await get_tenor(channel, "boobs")
            else:
                await channel.send("https://media.tenor.com/_ZvbLvrT_QcAAAAC/horny-jail-bonk.gif")
        else:
            await get_tenor(channel, "boobs")

async def f_my_ass_ta(bot, message, channel, req, upper_req):
    if req == "my-ass-ta":
        user = message.author.name

        if user != user_colton_name:
            # print(user)
            # print(user_colton_name)
            x = random.randint(3,5)
            if x == 5:
                await get_tenor(channel, "ass")
            else:
                await channel.send("https://media.tenor.com/_ZvbLvrT_QcAAAAC/horny-jail-bonk.gif")
        else:
            await get_tenor(channel, "ass")

async def f_carter(bot, message, channel, req, upper_req):
    if req == "carter":
        user_id = message.author.id
        print(user_id)
        if (user_id != user_carter_id):
            # print(user)
            # print(user_colton_name)
            # x = random.randint(3,5)
            # if x == 5:
            #     await get_tenor(channel, "feet")
            # else:
            #     await channel.send("https://tenor.com/view/veggie-tales-the-battle-is-not-ours-not-our-fight-esther-gif-16996193")
            await channel.send("https://tenor.com/view/veggie-tales-the-battle-is-not-ours-not-our-fight-esther-gif-16996193")
        else:
            await get_tenor(channel, "feet")

async def get_tenor(channel, search_term):
    apikey = "AIzaSyCiR3gYC7B1zsiROI1hz4Lx-5ObxMk-gkQ"
    limit = 50
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

async def f_persona(bot, message, channel, req, upper_req):
    if (req == "persona"):
        from links import links
        # send a random link from the file links.py
        await channel.send(random.choice(links.persona))

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
        # if upper_req.startswith("https://www.youtube.com/"):
        try:
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

            if voice_client.is_playing():
                voice_client.stop()

            ydl_opts = {
                'format': 'bestaudio/best',       
                'outtmpl': 'play-audio.mp3',       
                'noplaylist' : True,   
                'nooverwrites': False,        
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([upper_req])
            # source = discord.FFmpegOpusAudio(executable="C:\\Program Files\\ffmpeg\\ffmpeg-6.0-full_build\\bin\\ffmpeg.exe", source="youtube-audio.mp3", options="-b:a 64k")
            # voice_client.play(source)

            to_play = (discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\ffmpeg-6.0-full_build\\bin\\ffmpeg.exe", source="play-audio.mp3")))
            global pasta_volume
            to_play.volume = pasta_volume
            voice_client.play(to_play)

        except Exception as e:
            await channel.send("could not play that !!! (!pasta play <link>)")
            print(e)

async def f_download(bot, message, channel, req, upper_req):
    if req.startswith("download "):
        upper_req = upper_req[9:]
        # if upper_req.startswith("https://www.youtube.com/"):
        try:
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
                'outtmpl': 'download-audio.mp3',       
                'noplaylist' : True,   
                'nooverwrites': False,        
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([upper_req])
            
            await channel.send(file=discord.File("download-audio.mp3"))

        except:
            await channel.send("could not send that audio file !!!")

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
                await channel.send(f"damn {message.author.mention}, you got a shiny!")
                return

        if shiny_chance == 5:
            pic = requests.get(poke).json().get("sprites").get("other").get("official-artwork").get("front_shiny")
            if message.author.name == user_parker_name:
                await channel.send(pic)
                await channel.send(f"hey Mr. P-Man! {message.author.mention}, you got another shiny! (are you tryna make ur whole pokedex shiny???)")
            else:
                await channel.send(pic)
                await channel.send(f"damn {message.author.mention}, you got a shiny!")
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
        
acceptable_apologies = ["I would like some better odds Pasta! Please increase them."]

# async def f_emily(bot, message, channel, req, upper_req):
#     if req.startswith("emily"):
#         req = upper_req[6:]
#         if (message.author.name == user_emily_name) or message.author.name == user_colton_name:
#             if req in acceptable_apologies:
#                 import AuthorSendsMessage
#                 emilys_odds = AuthorSendsMessage.emilys_odds
#                 if (emilys_odds + 50) > 200:
#                     await channel.send("I can't increase your odds anymore! Sorry Emily.")
#                 else:
#                     await channel.send(f"Thank you!. Odds have been changed from 1 in {emilys_odds} to 1 in {emilys_odds + 50}.")
#                     emilys_odds += 50
#                     AuthorSendsMessage.emilys_odds = emilys_odds
#             else:
#                 await channel.send(f"That's not a valid request Ms. Lane. (hint: try `{acceptable_apologies[0]}`)")
#         else:
#             await channel.send("You're not emily, you can't change her odds for her.")

async def f_where_do_you_think_your_current_wife_is(bot, message, channel, req, upper_req):
    if req.startswith("where do you think your current wife is"):
        await channel.send("I'm not sure, I haven't concieved her yet")

async def f_emi(bot, message, channel, req, upper_req):
    # print(req)
    # print(req[3:])
    if req[:3] == "emi":
        global woohoo
        global waiting_for_emi
        global emi_responded
        # print("here")
        req = req[4:]
        if not ((message.author.name == user_emi_name) or (message.author.name == user_colton_name)):
            await channel.send("you cannot perform actions for emi!")
            return
        if req == "help":
            await channel.send("Hi Emi !! Please type `!pasta emi i took my meds pasta!` to respond when I ask you to take your meds!\n" +
                               "You can also see how long until I ask you to take your meds again by typing `!pasta emi wait time`")
            return
        if req == "i took my meds pasta!":
            if not waiting_for_emi:
                await channel.send("You're too early em!! I'll bug you again at 9:30pm.")
                return
            await channel.send(f"Thank you for taking your meds {message.author.mention}! I will bug you again at 9:30pm tomorrow <3")
            emi_responded = True
            return
        if req == "wait time":
            if waiting_for_emi:
                await channel.send("GO TAKE YOUR MEDS EMI")
                return
            time_now = datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time())
            datetime2 = datetime.datetime.combine(datetime.date.today(), woohoo)
            waiting_time = None
            # print(f"{time_now} | {datetime2}")
            if datetime2 < time_now:
               waiting_time = (datetime2 + datetime.timedelta(days=1)) - time_now
            else:
                waiting_time = datetime2 - time_now
            # print(waiting_time)

            total_seconds = int(waiting_time.total_seconds())

            # Compute the number of hours, minutes, and seconds in the timedelta
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)


            await channel.send(f"Emi has {hours} hours, {minutes} minutes, and {seconds} seconds left until I politely yell at her")
            return
        else:
            await channel.send("Invalid emi command Emi ! type `!pasta emi help` for help")
            return

async def f_set_volume(bot, message, channel, req, upper_req):
    volumes = {"quiet": 0.005, "semi-quiet": 0.013, "normal": 0.02, "kinda loud": 0.1, "loud": 0.3, "don't.": 1.0}
    if req == "set volume help":
        await channel.send("Valid volumes are: " + ", ".join(volumes.keys()) + "  ex. `!pasta set volume semi-quiet`")
        return
    if req.startswith("set volume "):
    #     if (message.author.name != user_colton_name):
    #         await channel.send("Only colton can change the volume rn, sorry (go yell at him or smthn)")
    #         return
        volumes = {"quiet": 0.005, "semi-quiet": 0.013, "normal": 0.02, "kinda loud": 0.1, "loud": 0.3, "don't.": 1.0}
        req = req[11:]
        vol = None
        if req in volumes:
            vol = volumes[req]
        else:
            await channel.send("Invalid volume! Valid volumes are: " + ", ".join(volumes.keys()))
        try:
            global pasta_volume
            pasta_volume = vol
            await channel.send(f"Volume set to {req}")
            print("volume = " + str(pasta_volume))
            return
        except:
            await channel.send("That volume didn't work for some reason")
    if req.startswith("set volume"):
        await channel.send("Valid volumes are: " + ", ".join(volumes.keys()) + "  ex. `!pasta set volume semi-quiet`")

async def play_a_source_file(bot, message, channel, req, source):
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
    
    if voice_client.is_playing():
        voice_client.stop()

    to_play = (discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\ffmpeg-6.0-full_build\\bin\\ffmpeg.exe", source=source)))
    global pasta_volume
    to_play.volume = pasta_volume
    voice_client.play(to_play)

async def f_dan_intro(bot, message, channel, req, upper_req):
    print(req)
    if req == ("dan intro"):
        await play_a_source_file(bot, message, channel, req, "musics/dan_mc_intro.mp3")

async def f_president_time(bot, message, channel, req, upper_req):
    if req == ("president time"):
        await play_a_source_file(bot, message, channel, req, "musics/president_time.mp3")
        
async def f_bretts_goofy_silly_side(bot, message, channel, req, upper_req):
    if req == ("bretts goofy silly side"):
        await play_a_source_file(bot, message, channel, req, "musics/brett_goofy_silly_side.mp3")