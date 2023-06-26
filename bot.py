import discord
from discord.ext import tasks
import requests

client = discord.Client()


@tasks.loop(seconds=2) # Повторяется каждые 2 секунды
async def my_loop(channel):
    data = requests.get('http://localhost:5000/api/orders').json()
    await channel.send(str(data))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # Мы передаем в функцию myLoop канал, чтобы иметь возможность отправлять сообщения
    if message.content == '$start':
        my_loop.start(message.channel)
    

client.run('OTc2OTI0NTU2MjA1OTEyMTQ1.G3z5hf.6QggktGfBOZdB4IaN5YVHt7d_dtFlrPzb3pZcI')