

import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='nim')
async def play_nim(ctx):
    await ctx.send("Still working on it, kiddo.")

bot.run(token)

print("Heyyyy")

@bot.command(name='coin_flip')
async def coin_flip():
    await ctx.send(random.choice(["Heads", "Tails"]))

bot.run(token)


@bot.command(name  = 'average')
async def average(nim1, nim2):
    await ctx.send(nim1 + nim2) / 2.0 

bot.run(token)



import random
def coin_flip():
  return random.choice(["Heads", "Tails"])

  print coin_flip