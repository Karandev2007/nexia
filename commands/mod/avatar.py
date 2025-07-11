import discord
from discord import app_commands

async def setup(tree: app_commands.CommandTree):
    @tree.command(name="avatar", description="Show a user's avatar")
    @app_commands.describe(user="User to get the avatar of")
    async def avatar_command(interaction: discord.Interaction, user: discord.User = None):
        target = user if user is not None else interaction.user
        avatar_url = target.display_avatar.url
        embed = discord.Embed(
            title=f"{target} Avatar",
            color=discord.Color.blurple()
        )
        embed.set_image(url=avatar_url)
        embed.add_field(name="Direct Link", value=f"[Click here]({avatar_url})", inline=False)
        await interaction.response.send_message(embed=embed) 