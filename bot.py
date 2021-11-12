import json
import os
import platform
import random
import sys
import bot_methods
import logging
import discord
from discord.ext import tasks
from discord.ext.commands import Bot

from config import config

intents = discord.Intents.default()
logging.basicConfig(level=logging.INFO)


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if not message.author == client.user:
            if message.content == '!help':
                print('Help method requested, firing')
                help_message = bot_methods.format_helper()
                await message.channel.send(help_message)
            prob = bot_methods.code_detection(message)
            print(message.content)
            if prob >= 3:
                await message.channel.send('Hey! Hope you don\'t mind me, I\'m just formatting your code for you! To '
                                           'learn more about this, type !help\n...' + '```' + message.content + '```')
            print(f'Code detection probability: {prob}')


client = MyClient()
client.run(config["token"])
