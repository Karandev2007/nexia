import discord
from discord import app_commands

async def setup(tree: app_commands.CommandTree):
    @tree.command(name="warn", description="Warn a member")
    @app_commands.describe(member="Member to warn", reason="Reason for warning")
    @app_commands.checks.has_permissions(moderate_members=True)
    async def warn_command(interaction: discord.Interaction, member: discord.Member, reason: str = None):
        if member == interaction.user:
            await interaction.response.send_message("You can't warn yourself <:CENNoMouthTurtle:1392845148970287145>", ephemeral=True)
            return
        try:
            embed = discord.Embed(
                title="Member Warned",
                description=f"<:Warning:1392860065349763082> {member.mention} That’s a warning! Behave yourself now.",
                color=discord.Color.gold()
            )
            if reason:
                embed.add_field(name="Reason", value=reason, inline=False)
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            await interaction.response.send_message(f"<:purpleween:1392860402924261550> uh a dark force interfered with your command ", ephemeral=True) 