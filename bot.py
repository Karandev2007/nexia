import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv
import importlib.util
import pathlib
import logging

# action logging
logging.basicConfig(
    filename='actions.log',
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def log_action(action: str, user: discord.User, target: discord.abc.User = None, reason: str = None, extra: str = None):
    msg = f"{user} (ID: {user.id}) performed {action}"
    if target:
        msg += f" on {target} (ID: {target.id})"
    if reason:
        msg += f" | Reason: {reason}"
    if extra:
        msg += f" | {extra}"
    logging.info(msg)

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
        raise ValueError("please set the TOKEN in .env file")
    bot.run(TOKEN)