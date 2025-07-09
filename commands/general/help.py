import discord
from discord import app_commands

async def setup(tree: app_commands.CommandTree):
    @tree.command(name="help", description="Get help with Nexia")
    async def help_command(interaction: discord.Interaction):
        embed = discord.Embed(
            title="**✨ Hey, I'm Nexia**",
            description=(
                "Your savvy partner in moderation, creativity, and whatever the future holds. I'm here to streamline the process."
            ),
            color=discord.Color.purple()
        )

        embed.add_field(
            name="📢 Need support?",
            value="Join our [Support Server](https://discord.gg/5B25KSvf)",
            inline=False
        )

        embed.set_footer(
            text="Made by QeinTech team",
            icon_url="https://iili.io/F1i8Cmu.md.png"
        )
        embed.set_thumbnail(url="https://iili.io/F1iksS9.png")

        await interaction.response.send_message(embed=embed, ephemeral=False)