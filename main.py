#====================================================
# FileName: main.py
# Description: MikuBot main script for Meguro
# Author: Narangelife
# Copyright: © Narange
#====================================================

# system
import os
from dotenv import load_dotenv

# discord
import discord
from discord.ext import commands

# environment
load_dotenv()
MIKUBOT_TOKEN = os.getenv('MIKUBOT_TOKEN')

#----------------------------------------------------
# Initialize

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='/', intents=intents)

#----------------------------------------------------
# Events

@bot.event
async def on_ready() -> None:
    print("[OnReady] MikuBot is ready")
    
    await bot.change_presence(activity=discord.Game(name="プロセカ"))
    
    
@bot.event
async def on_message(message: discord.Message) -> None:
    if message.author.bot:
        return # Ignore if the message sender is bot
    
    print("[OnMessage] Message received: {}".format(message.content))
    

#----------------------------------------------------
# Execute

bot.run(MIKUBOT_TOKEN)