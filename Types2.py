import discord
from discord.ext import commands
import stats
import Affects
import shiny_rate


def shiny(ctx, pokemon):
    for i in shiny_rate.data:
        if pokemon.capitalize() == i["pokemon"]:
            x = str(i['rate'])
            if x == " ":
                return "N/A"
            else:
                return f"{x}"


def weakness(ctx, pokemon):
    for i in Affects.data:
        if pokemon.capitalize() == i["pokemon_name"]:
            if len(i["weakness"].keys()) > 1:
                x = list(i["weakness"]["160"])
                y = list(i["weakness"]["256"])
                return f"{', '.join(x)}: Damage multiplier = {1.60}\n{', '.join(y)}: Damage multiplier = {2.56}"
            elif len(i["weakness"].keys()) == 1 and "160" in i["weakness"]:
                x = i["weakness"]["160"]
                return f"{', '.join(x)}: Damage multiplier = {1.6}"
            else:
                x = list(i["weakness"]["256"])
                return f"{', '.join(x)}: Damage multiplier = {2.56}"


def resistance(ctx, pokemon):
    for i in Affects.data:
        if pokemon.capitalize() == i["pokemon_name"]:
            if len(i["resistance"].keys()) > 1:
                x = i["resistance"]["62.5"]
                y = i["resistance"]["39"]
                return f"{', '.join(x)}: Damage multiplier = {0.625}\n{', '.join(y)}: Damage multiplier = {0.39}"
            elif len(i["resistance"].keys()) == 1 and "62.5" in i["resistance"]:
                x = list(i["resistance"]["62.5"])
                return f"{', '.join(x)}: Damage multiplier = {0.625}"
            else:
                x = i["resistance"]["39"]
                return f"{', '.join(x)}: Damage = {0.39}"


def types(ctx, pokemon):
    for i in stats.data:
        if pokemon.capitalize() == i["pokemon_name"]:
            x = i["main_type"]
            y = i["secondary_type"]
            if x and y is not None:
                return f"{x}\n{y}"


def number(ctx, pokemon):
    for i in stats.data:
        if pokemon.capitalize() == i['pokemon_name']:
            return i['number']


TOKEN = 'MTEzMjAzODI4NzcwODY2MzgwOA.GDLJcb.zHuxy8g1qOiC1XIoqB3hqH5F9o4j6R9hZmcGMM'

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command()
async def info(ctx, pokemon):
    embed = discord.Embed(
        title=f"{pokemon.capitalize()}",
        description=f"**Type:**\n{types(ctx, pokemon)}\n\n**Weakness:**\n{(weakness(ctx, pokemon))}\n\n**Resistance:**\n"
                    f"{resistance(ctx, pokemon)}\n\n**Wild Shiny Chance:**\n{shiny(ctx, pokemon)}",
        color=discord.Color.green())
    embed.set_thumbnail(url=f"https://github.com/HybridShivam/Pokemon/blob/master/assets/thumbnails-compressed/001.png")
    await ctx.send(embed=embed)


bot.run("MTEzMjAzODI4NzcwODY2MzgwOA.GDLJcb.zHuxy8g1qOiC1XIoqB3hqH5F9o4j6R9hZmcGMM")
