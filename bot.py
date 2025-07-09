import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv
import importlib.util
import pathlib

load_dotenv()

intents = discord.Intents.default()
ADMIN_ID = os.getenv("ADMIN_ID")
bot = commands.Bot(command_prefix=commands.when_mentioned_or(), intents=intents)
tree = bot.tree

async def load_commands():
    commands_path = pathlib.Path("commands")
    for category in commands_path.iterdir():
        if category.is_dir():
            for file in category.glob("*.py"):
                module_name = f"commands.{category.name}.{file.stem}"
                spec = importlib.util.spec_from_file_location(module_name, file)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                if hasattr(module, "setup"):
                    await module.setup(tree)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="with you :)"))
    await load_commands()
    try:
        synced = await tree.sync()
        print(f"globally synced {len(synced)} command(s)")
    except Exception as e:
        print(f"failed to globally sync commands: {e}")

if __name__ == "__main__":
    TOKEN = os.getenv("TOKEN")
    if not TOKEN:
        raise ValueError("please set the Token in .env.")
    bot.run(TOKEN)