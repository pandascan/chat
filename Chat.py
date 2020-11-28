import discord
from discord.ext import commands
import random
import time

bot = commands.Bot(command_prefix = "!", description = "Bot de Titouan")

@bot.event
async def on_ready():
	print("Ready !")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    Chan = bot.get_channel(774744523775410226)
    await Chan.send(f"> {message.content}\n{message.author}")
    await bot.process_commands(message)

@bot.event
async def on_message_delete(message):
	Chan = bot.get_channel(774744523775410226)
	await Chan.send(f"Le message de {message.author} a été supprimé \n> {message.content}")

@bot.event
async def on_message_edit(before, after):
	Chan = bot.get_channel(774744523775410226)
	await Chan.send(f"{before.author} a édité son message :\nAvant -> {before.content}\nAprès -> {after.content}")

bot.run("NzY5NTM4OTQ2MDEwODQxMDk4.X5Qe_g.1vMMMMADv-FCgPBCWClz9v6EmJE")
