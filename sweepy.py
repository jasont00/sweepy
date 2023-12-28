# bot.py
# A file to facilitate the connection to the Discord API.
import string
import discord
import os
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(
    name='sleeptime',
    help='Usage: !sleeptime *hour* *minute* *pm/am*.\nCalculates optimal waking up times.'
)
async def sleep(ctx, hour: int, minute: int, am_pm: str):
  currTime_str = currTime(hour, minute, am_pm)
  total_minutes = calcWakeUp(hour, minute, am_pm)
  out_str = currTime_str + printWakeUp(total_minutes) + " \nThese times account for 15 minutes to fall asleep. Goodnight!"
  await ctx.send(out_str)


# returns a string with the current time
def currTime(hour: int, minute: int, am_pm: str):
  out_str = "Current time is: "
  return out_str + timeStr(hour, minute, am_pm)


# calculates the time to wake up after 6 hours
def calcWakeUp(hour: int, minute: int, am_pm: str):
  hour = hour  # temp var
  # convert to 24 hour time
  if (am_pm.upper() == "AM"):
    if (hour == 12):
      hour = 0
  else:
    if (hour != 12):
      hour += 12
  # convert to minutes
  total_minutes = hour * 60 + minute
  # add recommended minimum sleep time (6 hours)
  total_minutes += 60 * 6
  return total_minutes


# prints output for wake up time (6, 7.5, 9 hours of sleep)
def printWakeUp(total_minutes: int):
  
  out_str = ""
  am_pm = ""
  for i in range(0, 3):
    total_minutes_temp = total_minutes % (60 * 24) + 15
    out_str += "\nYou should wake up at: "
    am_pm = "PM" if (total_minutes_temp / 2) >= 720 else "AM"
    temp = 90 * i
    total_minutes_temp += temp
    out_str += timeStr(total_minutes_temp // 60,
                       total_minutes_temp % 60, am_pm)
  return out_str


def timeStr(hour: int, minute: int, am_pm: str):
  out_str = ""
  out_str += str(hour%24) + ":"  # hour
  if (minute < 10):  # minutes
    out_str += "0" + str(minute)
  else:
    out_str += str(minute)
  out_str += " " + am_pm.upper()
  return out_str


if TOKEN:
  bot.run(TOKEN)
else:
  print("TOKEN not found. Please set the DISCORD_TOKEN environment variable.")
