import bot_methods
import logging
import discord

from config import config

intents = discord.Intents.default()
logging.basicConfig(level=logging.INFO)


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name='for code to format!'))

    async def on_message(self, message):
        if not message.author == client.user:
            prob = bot_methods.code_detection(message)
            print(message.content)
            if prob >= 3:
                await message.channel.send('Hey! Hope you don\'t mind me, I\'m just formatting your code for you! To '
                                           'learn more about this, type !!help\n...' + '```' + str(
                    message.content) + '```')
            print(f'Code detection probability: {prob}')
        if message.content == '!!help':
            print('Help method requested, firing')
            help_message = bot_methods.format_helper()
            await message.channel.send(help_message)


client = MyClient()
client.run(config["token"])
