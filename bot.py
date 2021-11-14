import bot_methods
import logging
import discord
from config import config

intents = discord.Intents.default()
logging.basicConfig(level=logging.INFO)


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        await client.change_presence(status=discord.Status.online,
                                     activity=discord.Activity(type=discord.ActivityType.listening, name='for code!'))

    async def on_message(self, message):

        if not message.author == client.user:
            lang_code = bot_methods.code_detection(message.content)
            if lang_code is not None:
                await message.channel.send('Hey! Hope you don\'t mind me, I\'m just formatting your code for you! To '
                                           f'learn more about this, type !!help\n```{lang_code}\n' + str(
                    message.content) + '```')
        if message.content == '!!help':
            help_message = bot_methods.format_helper()
            print('test gpg key')
            await message.channel.send(help_message)


client = MyClient()
client.run(config["token"])
