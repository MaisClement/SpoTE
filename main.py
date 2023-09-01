import discord
from discord.ext import commands
import subprocess
import sys
import os # default module
from dotenv import load_dotenv
import linecache
from random import choice
intents = discord.Intents.default()
intents.message_content = True
version = "1.0"
from selenium import webdriver
import geckodriver_autoinstaller

if os.name != 'nt': # Linux uniquement
    from pyvirtualdisplay import Display
    print ("Opening display")
    display = Display(visible=0, size=(1920, 1080)).start()

print ("Démarrage ...")

driver = webdriver.Firefox()

bot = discord.Bot()

print ("Firefox ✔")
@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="la version " + version))
@bot.slash_command(name="spot")
async def spot(ctx):
    try:
        embed = discord.Embed(
            description = '📷',
            color = discord.Color.from_rgb(16, 108, 138)
        )
        await ctx.respond("Spot en cours de chargement", ephemeral=True, delete_after=3)
        message = await ctx.channel.send(embed=embed)
        
        
        driver.set_window_size(1200, 484) 
        driver.get('https://mylines.fr/luca/spot')
        driver.save_screenshot('spot.png')

        with open('spot.png', "rb") as fh:
            f = discord.File(fh, filename='spot.png')
        await ctx.send(file=f)

        await message.delete()
    except Exception as e:
        await printerror(e, ctx)
        

async def printerror(e, ctx):

    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))

    embed = discord.Embed(
        description = ':red_circle: Quelque chose s\'est mal passé',
        color = discord.Color.from_rgb(215, 2, 2)
    )    
    await ctx.channel.send(embed=embed)
load_dotenv()
bot.run(os.getenv('TOKEN'))