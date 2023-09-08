import os
import disnake
from disnake.ext import commands
import json
import openai

with open('config.json') as f:
    data = json.load(f)
    token = data["token"]
    prefix = data["prefix"]
    openai.api_key = data["gpt_token"]

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix=prefix, help_command=None, intents=intents)

@bot.event
async def on_ready():
    print("Ваша виртуальная ассистентка запущена!")
    for filename in os.listdir('cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(token)