import discord
from discord import app_commands
from discord.utils import get
import logging

async def setup(tree: app_commands.CommandTree):
    @tree.command(name="lock", description="Lock the current channel")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def lock_command(interaction: discord.Interaction):
        channel = interaction.channel
        if not isinstance(channel, discord.TextChannel):
            await interaction.response.send_message("<:Warning:1392860065349763082> This command can only be used in text channels.", ephemeral=True)
            return
        everyone_role = get(interaction.guild.roles, name="@everyone") # you can replace this with your own role like member or users etc, make sure to change in both lock/unlock files :D
        try:
            await channel.set_permissions(everyone_role, send_messages=False)
            embed = discord.Embed(
                title="Channel Locked",
                description=f"<:lock_IDS:1393628240328785931> The gates to {channel.mention} have been sealed. Only the high council may now speak.",
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed)
            # log action
            if "log_action" in globals():
                log_action("lock", interaction.user, extra=f"Channel: {channel.name}")
        except discord.Forbidden:
            await interaction.response.send_message("<:PepeWitch:1393629420312596641> The magic required to lock this space is beyond my grasp.", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"<:Warning:1392860065349763082> uh a dark force interfered with your command ", ephemeral=True)