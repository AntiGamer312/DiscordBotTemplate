import discord
from discord import app_commands
from client import client

@client.tree.command(name="test", description="test", guild=client.guildId)
async def test(interaction : discord.Interaction):
    await interaction.response.send_message("Nike")