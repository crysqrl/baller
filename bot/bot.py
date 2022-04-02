import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands

ITK_PREFIX = r'https://www.itkkit.ru/'
TOKEN = 'TOKEN_WAS_HERE'

bot = commands.Bot(command_prefix='>')


@bot.command()
async def hi(ctx):
    if ctx.channel.name == 'bot' or ctx.channel.name == 'general':
        await ctx.send('ballin')


@bot.command()
async def itk_sale(ctx):
    if ctx.channel.name == 'bot' or ctx.channel.name == 'general':
        html = requests.get(r'https://www.itkkit.ru/catalog/sale/?SHOWALL_1=1')
        soup = BeautifulSoup(html.content)
        items = soup.find_all('li', class_='products_item')
        item = items[1]
        img = ITK_PREFIX + item.find('img').get('src', None)
        title = item.find('div', class_='product_h_title').text
        position = item.find('div', class_='product_h_position').text
        old_price = item.find('span', class_='old_price').text
        new_price = item.find('span', class_='current_price').text
        embed = discord.Embed()
        embed.set_thumbnail(url=img)
        embed.add_field(name='title', value=title, inline=False)
        embed.add_field(name='position', value=position, inline=False)
        embed.add_field(name='old price', value=old_price, inline=False)
        embed.add_field(name='new price', value=new_price, inline=False)
        await ctx.send(embed=embed)


bot.run(TOKEN)
