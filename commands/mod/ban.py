import discord
from discord import app_commands

async def setup(tree: app_commands.CommandTree):
    @tree.command(name="ban", description="Ban a member")
    @app_commands.describe(member="Member to ban", reason="Reason for ban")
    @app_commands.checks.has_permissions(ban_members=True)
    async def ban_command(interaction: discord.Interaction, member: discord.Member, reason: str = None):
        if member == interaction.user:
            await interaction.response.send_message("Hey! you can't friendly fire yourself outta the server <:CENNoMouthTurtle:1392845148970287145>", ephemeral=True)
            return
        try:
            await member.ban(reason=reason)
            embed = discord.Embed(
                title="Member Banned",
                description=f"<:BanHammer:1392846415751024705> {member.mention} has been kicked into the void.",
                color=discord.Color.red()
            )
            if reason:
                embed.add_field(name="Reason", value=reason, inline=False)
            await interaction.response.send_message(embed=embed)
        except discord.Forbidden:
            await interaction.response.send_message("<:Info:1392846629710598328> Looks like target is immune to ban attempts", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"<:purpleween:1392860402924261550> uh a dark force interfered with your command ", ephemeral=True) 