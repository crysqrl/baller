import discord
from discord.ext import commands

TOKEN = 'NTkwNDgxMzE5Mjc2OTY5OTg0.XQi63Q.2-5a7Wa3jlZLQUEkiRSnmNvfnvM'

bot = commands.Bot(command_prefix='>')


@bot.command()
async def hi(ctx):
    await ctx.send('ballin')

bot.run(TOKEN)
