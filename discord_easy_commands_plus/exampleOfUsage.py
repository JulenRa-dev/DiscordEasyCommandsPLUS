import os
import discord
from discord_easy_commands_plus import EasyBotPlus

intents = discord.Intents.default()
intents.message_content = True

bot = EasyBotPlus(intents=intents)
bot.setCommand("!help",["mYou can use !hello to make me say hello", "Or you can use !goodbye to make me say goodbye"])
bot.setCommand("!hello",["mHello"])
bot.setCommand("!goodbye",["mGoodbye"])
bot.setCommand("!startDm",["wHello at DM"]
bot.run(os.environ["TOKEN"]) #This part of "os.environ["TOKEN"] is because this must run on replit, and you must add your token as a Secret
