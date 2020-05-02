import sys
import signal
import os
import discord
import asyncio
from mcstatus import MinecraftServer
from dotenv import load_dotenv
from discord.ext import commands, timers
from datetime import datetime, timedelta


load_dotenv(override=True)
TOKEN            = os.getenv('DISCORD_TOKEN')
STATUS_CHANNEL   = os.getenv('DISCORD_STATUS_CHANNEL')
MINECRAFT_SERVER = os.getenv('MINECRAFT_SERVER')
TICK_INTERVAL    = os.getenv('STATUS_INTERVAL_SECONDS', default=10)
MCDISCORD_DEBUG  = os.getenv('MCDISCORD_DEBUG', default=False)

if TOKEN is None or MINECRAFT_SERVER is None:
    print('Error: DISCORD_TOKEN and MINECRAFT_SERVER must be set.')
    print('Did you create an .env file?')
    sys.exit(-1)

if MCDISCORD_DEBUG:
    if str(MCDISCORD_DEBUG).lower() in ["off", "false", "0", "no"]:
        MCDISCORD_DEBUG = False
    else:
        MCDISCORD_DEBUG = True

server = MinecraftServer.lookup(MINECRAFT_SERVER)
bot = commands.Bot(command_prefix='!')
channel = None

async def send_channel_message(channel, message):
    if channel is not None:
        await channel.send(message)

    if MCDISCORD_DEBUG:
        print("DEBUG: {0}".format(message), file=sys.stderr)

async def status_task():
    global channel

    connected      = False
    prev_players   = None
    prev_connected = False

    if STATUS_CHANNEL is not None and len(STATUS_CHANNEL):
        try:
            channel = await bot.fetch_channel(STATUS_CHANNEL)
        except:
            print(f'ERROR: unable to find channel {STATUS_CHANNEL}')
            channel = None

    if channel is not None:
        if MCDISCORD_DEBUG:
            print("DEBUG: got channel.", file=sys.stderr)

    while True:
        try:
            status = server.status()
            connected = True
            if prev_connected is not True:
                prev_connected = True
                await send_channel_message(channel, "Minecraft server online.")

            players_online = status.players.online
            players_max = status.players.max
        except ConnectionRefusedError:
            connected = False
            if prev_connected is not False:
                prev_players = None
                await send_channel_message(channel, "Minecraft server offline?")

        if connected is True:
            if prev_players != players_online:
                status_msg = "Online: {0}/{1} players".format(players_online, players_max)
                game = discord.Game(status_msg)
                await bot.change_presence(activity=game)
                await send_channel_message(channel, "Server Status: {0}".format(status_msg))
                prev_players = players_online
        else:
            if prev_connected is not False:
                prev_connected = False
                game = discord.Game("Server Offline")
                await bot.change_presence(activity=game)

        await asyncio.sleep(TICK_INTERVAL)

def shutdown():
    print("Shutting down, please wait...", file=sys.stderr)
    bot.loop.stop()

@bot.event
async def on_ready():
    game = discord.Game("WAITING")
    await bot.change_presence(activity=game)
    print(f'{bot.user.name} has connected to Discord!')
    print('Press Ctrl-C to exit.')
    bot.loop.create_task(status_task())
    try:
        bot.loop.add_signal_handler(signal.SIGINT, shutdown)
        bot.loop.add_signal_handler(signal.SIGTERM, shutdown)
        #bot.loop.add_signal_handler(signal.SIGTERM, lambda: bot.loop.stop())
    except NotImplementedError:
        pass

bot.run(TOKEN)
