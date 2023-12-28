# bot.py
# A file to facilitate the connection to the Discord API.
import discord
import os
from functions import *
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(
    name='sleep',
    help='Usage: !sleep *hour* *minute* *pm/am*.\nCalculates optimal waking up times.'
)
async def sleep(ctx, hour: int, minute: int, am_pm: str):
  currTime_str = currTime(hour, minute, am_pm)
  total_minutes = calcWakeUp(hour, minute, am_pm)
  out_str = currTime_str + printWakeUp(total_minutes) + " \nThese times account for 15 minutes to fall asleep. Goodnight!"
  await ctx.send(out_str)


@bot.command(
    name='wakeup',
    help='Usage: !wakeup *hour* *minute* *pm/am.\nCalculates optimal sleeping times.'
)
async def wakeUp(ctx, hour: int, minute: int, am_pm: str):
  wakeupTime_str = wakeupTime(hour, minute, am_pm)
  total_minutes = calcSleepTime(hour, minute, am_pm)
  out_str = wakeupTime_str + printSleepTime(total_minutes) + " \nThese times account for 15 minutes to fall asleep. Goodnight!"
  await ctx.send(out_str)
  



if TOKEN:
  bot.run(TOKEN)
else:
  print("TOKEN not found. Please set the DISCORD_TOKEN environment variable.")
