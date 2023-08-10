#This was made using by base the discord_easy_commands library
#So i would like to give credits to Linkfy, the person who originally made this
#Anyways, the mod is made by me, JulenRa or JRaDev or JulenRa-dev

import discord
from flask import Flask
from threading import Thread
import random

class EasyBotPlus(discord.Client):
    __commands = []
    app = Flask('')

    @app.route('/')
    def home():
        return "Hello, The bot is running!"
    def runServer(self):
        self.app.run(host='0.0.0.0', port=8181)
    def keep_alive(self):
        t = Thread(target=self.runServer)
        t.start()
    async def on_ready(self):
        print("Bot acitvated! {0}".format(self.user))

    async def on_message(self, message):
      succes = random.randint(1,1000)
      if succes == -1:
        succes = -2
        await message.channel.send("Sorry, but i'm not feeling like doing what's expected now")
      elif succes == -2:
        return
      else:
        for command in self.__commands:
            if(message.content == command[0]):
                print("Channel: {0.channel} | User {0.author} : {0.content}".format(message))
                for i in range(len(command[1])):
                  typeNotDefined = True
                  type = None
                  if command[1][i][0:1] == "m":
                    type = "msg"
                    typeNotDefined = False
                  elif command[1][i][0:1] == "w":
                    type = "warn"
                    typeNotDefined = False
                  if typeNotDefined:
                    await message.channel.send("[**DEBUG**]: Value isn't valid")
                  else:
                    if type == "msg":
                      await message.channel.send(command[1][i][1:len(command[1][i])])
                    elif type == "warn":
                      user = message.author
                      dm_channel = await user.create_dm()
                      await dm_channel.send(command[1][i][1:len(command[1][i])])
                  #await message.channel.send(command[1][i])
    def setCommand(self, command, text):
        new_command = (command, text)
        self.__commands.append(new_command)
    def run(self, token):
        self.setCommand("!powered",["mI'm running using the discord_easy_commands_plus python library, that is not aviable on pip yet."])
        self.keep_alive()
        return super().run(token)
