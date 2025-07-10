import discord
from discord import app_commands
from datetime import timedelta

async def setup(tree: app_commands.CommandTree):
    @tree.command(name="timeout", description="Timeout a member")
    @app_commands.describe(member="Member to timeout", duration="Timeout duration in minutes", reason="Reason for timeout")
    @app_commands.checks.has_permissions(moderate_members=True)
    async def timeout_command(interaction: discord.Interaction, member: discord.Member, duration: int, reason: str = None):
        if member == interaction.user:
            await interaction.response.send_message("You can't timeout yourself <:CENNoMouthTurtle:1392845148970287145>", ephemeral=True)
            return
        try:
            until = discord.utils.utcnow() + timedelta(minutes=duration)
            await member.timeout(until, reason=reason or "")
            embed = discord.Embed(
                title="Member Timed Out",
                description=f"<:Timeout:1392861018408878080> {member.mention} has been put in timeout for {duration} minutes.",
                color=discord.Color.purple()
            )
            if reason:
                embed.add_field(name="Reason", value=reason, inline=False)
            await interaction.response.send_message(embed=embed)
        except discord.Forbidden:
            await interaction.response.send_message("<:Info:1392846629710598328> Looks like target is immune to timeout attempts", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"<:purpleween:1392860402924261550> uh a dark force interfered with your command ", ephemeral=True)  