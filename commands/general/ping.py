import discord
from discord import app_commands

async def setup(tree: app_commands.CommandTree):
    @tree.command(name="ping", description="Check Nexia's latency")
    async def ping_command(interaction: discord.Interaction):
        latency = round(interaction.client.latency * 1000)
        await interaction.response.send_message(f"Ping confirmed! I'm active and well at {latency}ms.", ephemeral=True)