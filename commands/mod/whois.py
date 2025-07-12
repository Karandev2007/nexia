import discord
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()
ADMIN_ID = os.getenv("ADMIN_ID")

async def setup(tree: app_commands.CommandTree):
    @tree.command(name="whois", description="Get user information")
    @app_commands.describe(user="User to get info about")
    async def whois_command(interaction: discord.Interaction, user: discord.Member = None):
        if str(interaction.user.id) != str(ADMIN_ID): # need to be admin
            await interaction.response.send_message("<:Info:1392846629710598328> You do not have permission to use this command.", ephemeral=True)
            return
        target = user or interaction.user
        embed = discord.Embed(
            title=f"<:Help_Icon:1207931111553105982> {target.display_name} Information",
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=target.display_avatar.url)
        embed.add_field(name="Username", value=str(target), inline=True)
        embed.add_field(name="User ID", value=target.id, inline=True)
        embed.add_field(name="Mention", value=target.mention, inline=True)
        embed.add_field(name="Account Created", value=target.created_at.strftime('%Y-%m-%d %H:%M:%S'), inline=True)
        if hasattr(target, 'joined_at') and target.joined_at:
            embed.add_field(name="Joined Server", value=target.joined_at.strftime('%Y-%m-%d %H:%M:%S'), inline=True)
        if hasattr(target, 'roles'):
            roles = [role.mention for role in target.roles if role.name != "@everyone"] # dont add everyome role
            embed.add_field(name="Roles", value=", ".join(roles) if roles else "None", inline=False)
        await interaction.response.send_message(embed=embed)