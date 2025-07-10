import discord
from discord import app_commands, PartialEmoji

# intro page
def get_home_embed():
    embed = discord.Embed(
        title="**✨ Hey, I'm Nexia**",
        description="Your sharp, reliable partner for moderation, creativity, and whatever comes next — here to keep things running smoothly.",
        color=discord.Color.purple()
    )
    embed.add_field(
        name="📢 Need support?",
        value="Join our [support server](https://discord.gg/PuyDG8v6TC) or check out the buttons below.",
        inline=False
    )
    embed.set_footer(
        text="Made by QeinTech team",
        icon_url="https://iili.io/F1i8Cmu.md.png"
    )
    embed.set_thumbnail(url="https://iili.io/F1iksS9.png")
    return embed

# drop menu
class HelpDropdown(discord.ui.Select):
    def __init__(self, bot_id: int):
        self.bot_id = bot_id
        options = [
            discord.SelectOption(
                label="Home",
                description="Overview of Nexia",
                emoji=PartialEmoji(name="nexia_home", id=1392704215398482122)
            ),
            discord.SelectOption(
                label="Commands",
                description="See what commands you can use",
                emoji=PartialEmoji(name="nexia_commands", id=1392704368729526283)
            )
        ]
        super().__init__(placeholder="Select a page", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Home":
            await interaction.response.edit_message(embed=get_home_embed(), view=self.view)

        elif self.values[0] == "Commands":
            embed = discord.Embed(
                title="<:blurple_slashcommands:1392704368729526283> **Nexia Commands**",
                    description=(
                    "**General**\n"
                    "``help``, ``invite``, ``ping``\n\n"
                    "**Moderation**\n"
                    "``ban``, ``kick``, ``warn``, ``timeout``\n"
            ),
                color=discord.Color.purple()
            )
            embed.set_footer(
                text="Made by QeinTech team",
                icon_url="https://iili.io/F1i8Cmu.md.png"
            )
            embed.set_thumbnail(url="https://iili.io/F1iksS9.png")
            await interaction.response.edit_message(embed=embed, view=self.view)

# footer butttons
class HelpView(discord.ui.View):
    def __init__(self, bot_id: int):
        super().__init__(timeout=None)
        self.add_item(HelpDropdown(bot_id))

        self.add_item(discord.ui.Button(
            label="Invite",
            url=f"https://discord.com/oauth2/authorize?client_id={bot_id}&permissions=8&scope=bot%20applications.commands",
            emoji=PartialEmoji(name="nexia_invite", id=1392687772669710406)
        ))

        self.add_item(discord.ui.Button(
            label="Visit Website",
            url="https://qeintech.in",
            emoji=PartialEmoji(name="nexia_web", id=1392702061413531680)
        ))

        self.add_item(discord.ui.Button(
            label="Support Server",
            url="https://discord.gg/5B25KSvf",
            emoji=PartialEmoji(name="nexia_support", id=1392702248005406770)
        ))


async def setup(tree: app_commands.CommandTree):
    @tree.command(name="help", description="Get help with Nexia")
    async def help_command(interaction: discord.Interaction):
        bot_id = interaction.client.user.id
        view = HelpView(bot_id)
        await interaction.response.send_message(embed=get_home_embed(), view=view, ephemeral=False)