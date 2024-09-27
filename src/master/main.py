import os
from sys import exit

from dotenv import load_dotenv
import discord

load_dotenv()

def main():
    bot_token = os.environ.get("DISCORD_TOKEN")
    if bot_token is None:
        print_error("Bot token is not define")
        exit(1)

    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('!start'):
            if message.author.voice is None:
                await message.channel.send('Вы не в канале')

            voice_channel = message.author.voice.channel
            if voice_channel is None:
                await message.channel.send('Вы не в канале')
                return

            await voice_channel.connect()

        if message.content.startswith('!end'):
            voice_client = message.guild.voice_client
            if voice_client.is_connected():
                await voice_client.disconnect()
                print("Bot disconnected from voice channel.")
            else:
                print("Bot is not connected to a voice channel.")

        if message.content.startswith('!ping'):
            await message.channel.send('pong')

    client.run(bot_token)


def print_error(error: str):
    print(f"\u001b[31m{error}\u001b[0m")


if __name__ == "__main__":
    main()
