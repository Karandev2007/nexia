import discord
from discord import app_commands

async def setup(tree: app_commands.CommandTree):
    @tree.command(name="kick", description="Kick a member")
    @app_commands.describe(member="Member to kick", reason="Reason for kick")
    @app_commands.checks.has_permissions(kick_members=True)
    async def kick_command(interaction: discord.Interaction, member: discord.Member, reason: str = None):
        if member == interaction.user:
            await interaction.response.send_message("You can't launch yourself outta the server <:CENNoMouthTurtle:1392845148970287145>", ephemeral=True)
            return
        try:
            await member.kick(reason=reason or "")
            embed = discord.Embed(
                title="Member Kicked",
                description=f"<:Boot:1392846415751024705> {member.mention} has been shown the door.",
                color=discord.Color.orange()
            )
            if reason:
                embed.add_field(name="Reason", value=reason, inline=False)
            await interaction.response.send_message(embed=embed)
        except discord.Forbidden:
            await interaction.response.send_message("<:Info:1392846629710598328> Looks like target is immune to kick attempts", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"<:purpleween:1392860402924261550> uh a dark force interfered with your command ", ephemeral=True)  