import discord
from discord import app_commands

class InviteView(discord.ui.View):
    def __init__(self, url: str):
        super().__init__()
        self.add_item(discord.ui.Button(label="🔗 Invite Nexia", url=url))

async def setup(tree: app_commands.CommandTree):
    @tree.command(name="invite", description="Get Nexia's invite link")
    async def invite_command(interaction: discord.Interaction):
        bot_id = interaction.client.user.id
        link = f"https://discord.com/oauth2/authorize?client_id=1160519036631797820&permissions=8&scope=bot%20applications.commands"
        view = InviteView(url=link)
        await interaction.response.send_message("Ready to roll? Click the button and let Nexia join the crew. <:nexia:1392688452516184075>", view=view, ephemeral=True)