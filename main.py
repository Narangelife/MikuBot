#====================================================
# FileName: main.py
# Description: MikuBot main script for Meguro
# Author: Narangelife
# Copyright: © Narange
#====================================================

# system
import os
from dotenv import load_dotenv
from typing import Union

# discord
import discord
from discord import app_commands
from discord.ext import commands

# custom
from config import getRoleId

# environment
load_dotenv()
MIKUBOT_TOKEN = os.getenv('MIKUBOT_TOKEN')
MIKUBOT_GUILD_ID = os.getenv('MIKUBOT_GUILD_ID')

#----------------------------------------------------
# Initialize

intents = discord.Intents.all()

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client=client)

guild = discord.Object(MIKUBOT_GUILD_ID)

#----------------------------------------------------
# Events

@client.event
async def on_ready() -> None:
    print("[OnReady] MikuBot is ready")
    
    await client.change_presence(activity=discord.Game(name="プロセカ"))
    tree.clear_commands(guild=None)
    await tree.sync(guild=guild)
    
    
@client.event
async def on_message(message: discord.Message) -> None:
    if message.author.bot:
        return # Ignore if the message sender is bot
    
    print("[OnMessage] Message received: {}".format(message.content))
    
    
@client.event
async def on_reaction_add(reaction: discord.Reaction, user: Union[discord.Member, discord.User]):
    if user.bot:
        return # Ignore if the message sender is bot
    
    print("[OnReaction] Add message received: {} (by {}), count: {}".format(reaction.emoji, user.name, reaction.count))
    
    if reaction.emoji == "📌" and not reaction.message.pinned:
        await reaction.message.pin()
        print("[OnReaction] Pined!")
    
    
@client.event
async def on_reaction_remove(reaction: discord.Reaction, user: Union[discord.Member, discord.User]):
    if user.bot:
        return # Ignore if the message sender is bot
    
    print("[OnReaction] Remove message received: {} (by {}), count: {}".format(reaction.emoji, user.name, reaction.count))
    
    if reaction.emoji == "📌" and reaction.message.pinned and reaction.count == 0:
        await reaction.message.unpin()
        print("[OnReaction] Remove pin!")
    
    
#----------------------------------------------------
# SlashCommand
# [Interaction Reference] https://discordpy.readthedocs.io/ja/latest/interactions/api.html

@tree.command(name="dev", description="試験用コマンド")
async def dev_command(interaction: discord.Interaction) -> None:
    await interaction.response.send_message("Message: {}".format(interaction.message), ephemeral=True)
    
    
@tree.command(name="sudo", description="管理者用コマンド")
@app_commands.default_permissions(administrator=True)
async def sudo_command(interaction: discord.Interaction) -> None:
    await interaction.response.send_message("Admin", ephemeral=True)
    
    
@tree.command(name="year", description="入学年度ロール設定")
@app_commands.describe(year="入学年度 西暦 下位2桁 (10進数)", operation="操作")
@app_commands.choices(operation = [
    app_commands.Choice(name="付与", value=0),
    app_commands.Choice(name="剥奪", value=1)
])
async def year_command(interaction: discord.Interaction, year: int = None, operation: app_commands.Choice[int] = None):
    role_id = getRoleId(year)
    embed = discord.Embed()
    
    embed.title = "Failed"
    embed.description = "入学年度の指定が不正です"
    embed.color = 0xff3248
    
    if role_id != -1:
        print("[year] Year: {}, RoleId: {}, Operation: {}".format(year, role_id, operation))
        op_role = interaction.guild.get_role(role_id)
        if operation == 0:
            await interaction.user.add_roles(op_role)
            embed.title = "Success"
            embed.description = "{}生ロールを付与しました".format(year)
            embed.color = 0x2cffec
        elif operation == 1:
            await interaction.user.remove_roles(op_role)
            embed.title = "Success"
            embed.description = "{}生ロールを剥奪しました".format(year)
            embed.color = 0xd437ff
        else:
            embed.description = "操作内容の指定が不正です"
    
    await interaction.response.send_message(embed=embed)


#----------------------------------------------------
# Execute

client.run(MIKUBOT_TOKEN)