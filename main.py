import discord
from discord.ext import commands
from model import get_class


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()    
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save (f"./{attachment.filename}")
            class_name, confidence_score = get_class('keras_model.h5', 'labels.txt', f'./{attachment.filename}')
            await ctx.send(f'File: {file_name}\nClass: {class_name}\nConfidence Score: {confidence_score:.2f}')
    else:
            await ctx.send("No as subido nada.")
            

bot.run("MTUwMTc0OTc5NzUxNjc0Mjc0Ng.Gb1qR3.v2zZNK5N_wI1kV5PhWNmMjMDQpFROggKTxhaHo")