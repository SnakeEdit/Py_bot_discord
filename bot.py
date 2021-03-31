import discord
import datetime
now = datetime.datetime.now()
today = datetime.datetime.today()
from discord.ext import commands

TOKEN = "take from site"

bot = commands.Bot(command_prefix=('+'))
bot.remove_command( 'help' )

@bot.event
async def on_ready():
    print("Зачем меня призвали?")
@bot.command()
async def time(ctx):
    await ctx.send(today.strftime("Текущее время в Волгограде - %H:%M:%S"))

bot.run(TOKEN)