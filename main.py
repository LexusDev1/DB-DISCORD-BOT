import nextcord
import os
import asyncio
import yaml
from nextcord.ext import commands

with open("config.yaml") as config:
    CONFIG = yaml.safe_load(config)

TOKEN = CONFIG['DISCORD_CREDENTIALS']['TO']
PREFIX = CONFIG['DISCORD_CREDENTIALS']['PREFIX']


intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

client = nextcord.Bot(command_prefix=PREFIX, intents=intents)

async def load():
    for foldername in os.listdir("./cogs/{foldername}"):
        for filename in os.listdir("./cogs/{filename}"):
            if filename.endswith(".py"):
                client.load_extension("cogs.{filename[:-3]}")

async def main():
    await load()
    await client.start(TOKEN)

asyncio.run(main())