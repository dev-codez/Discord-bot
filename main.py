from discord.ext import commands
import discord
import json
from pathlib import Path
import os

bot = commands.Bot(command_prefix=">", help_command=None)
config = json.load(open("config.json"))




@bot.event
async def on_ready():
    print("Bot is ready")
    print(f"discord.py version is {discord.__version__}")

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        try:
            bot.load_extension(f"cogs.{file[:-3]}")
            print(f"{file} is loaded")
        except:
            print(f"Error occured while loading {file}")


try:
    bot.run(config["token"])
except Exception as e:
    print(f"there was error starting the bot probably something to do with the token")