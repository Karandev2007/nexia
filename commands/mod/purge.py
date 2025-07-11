import discord
from discord import app_commands

async def setup(tree: app_commands.CommandTree):
    @tree.command(name="purge", description="Delete multiple messages from this channel")
    @app_commands.describe(amount="Number of messages to delete (max 100)")
    @app_commands.checks.has_permissions(manage_messages=True)
    async def purge_command(interaction: discord.Interaction, amount: int):
        channel = interaction.channel
        if not isinstance(channel, (discord.TextChannel, discord.Thread)):
            await interaction.response.send_message("This command can only be used in text channels or threads.", ephemeral=True)
            return
        if amount < 1 or amount > 100:
            await interaction.response.send_message("Please specify an amount between 1 and 100.", ephemeral=True)
            return
        try:
            deleted = await channel.purge(limit=amount)
            embed = discord.Embed(
                title="Messages Purged",
                description=f"<:Purge:1392846415751024705> {len(deleted)} messages gobbled up by the void.",
                color=discord.Color.dark_teal()
            )
            await interaction.response.send_message(embed=embed, ephemeral=False)
        except discord.Forbidden:
            await interaction.response.send_message("<:Info:1392846629710598328> Nope! i cant play cleanup crew in this room.", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"<:Info:1392846629710598328> No effect. The command was rejected by the forces beyond. ", ephemeral=True) 