import discord
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()
ADMIN_ID = os.getenv("ADMIN_ID")

async def setup(tree: app_commands.CommandTree):
    @tree.command(name="say", description="Make the bot say something")
    @app_commands.describe(message="The message to say")
    async def say_command(interaction: discord.Interaction, message: str):
        if str(interaction.user.id) != str(ADMIN_ID):
            await interaction.response.send_message("The ancient wards deny you access to this power <:SkaryHalloweenPumpkin:1167705320118816768>", ephemeral=True)
            return
        await interaction.response.send_message(message) 