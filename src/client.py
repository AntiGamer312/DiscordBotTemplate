import discord
from discord.ext import commands
from discord import app_commands
from os import getenv
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = str(getenv("DISCORD_BOT_TOKEN"))
DISCORD_SERVER_ID = int(getenv("DISCORD_SERVER_ID"))  # type: ignore

print(type(DISCORD_SERVER_ID))

class Client(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(
            command_prefix=command_prefix,
            intents=intents
        )
        self.serverId : int | None = None
        self.guildId : discord.Object | None = None

    async def on_ready(self):
        print(f"Logged on as {self.user}")

        try:
            synced = await self.tree.sync(guild=self.guildId)
            print(f"Synced {len(synced)} commands")
        except Exception as e:
            print(f"Error : {e}")

    async def on_message(self, message : discord.Message):
        print(f"{message.author} : {message.content}")

intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)
client.serverId = DISCORD_SERVER_ID
client.guildId = discord.Object(DISCORD_SERVER_ID)

import commands #This weird doohickey

client.run(DISCORD_TOKEN)