from discord.ext import commands
import discord


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.command()
async def start(ctx):
    if ctx.author.voice is None:
        await ctx.send('Вы не в канале')

    voice_channel = ctx.author.voice.channel
    if voice_channel is None:
        await ctx.send('Вы не в канале')
        return

    await voice_channel.connect()


@bot.command()
async def end(ctx):
    voice_client = ctx.guild.voice_client

    if voice_client.is_connected():
        await voice_client.disconnect()
        await ctx.send("Бот отключился от голосового канала")
        return
    
    ctx.send("Бот не подключён к голосовому каналу")