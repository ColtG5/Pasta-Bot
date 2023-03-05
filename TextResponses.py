import requests
import discord
from gtts import gTTS

greetings = ["hi", "hey", "hello"]
farewells = ["bye", "cya", "goodbye", "good bye"]

async def f_hello(bot, message, channel, req):
    if req in greetings:
        await channel.send("Hello human!")

async def f_goodbye(bot, message, channel, req):
    if req in farewells:
        await channel.send("Goodbye Human.")

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