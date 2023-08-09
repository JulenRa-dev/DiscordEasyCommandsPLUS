import os
import discord
from discord_easy_commands_plus import EasyBotPlus

intents = discord.Intents.default()
intents.message_content = True

bot = EasyBotPlus(intents=intents)
bot.setCommand("!help",["You can use !hello to make me say hello", "Or you can use !goodbye to make me say goodbye"])
bot.setCommand("!hello",["Hello"])
bot.setCommand("!goodbye",["Goodbye"])
bot.run(os.environ["TOKEN"]) #This part of "os.environ["TOKEN"] is because this must run on replit, and you must add your token as a Secret
