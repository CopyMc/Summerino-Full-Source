import discord
from discord.ext import commands
from config import BOT_TOKEN, PREFIX
from database import Database
import asyncio
import os

# Creator And Developer : Copy
async def load_cogs(bot):
    cogs = [
        'economy',
        'games', 
        'music',
        'images',
        'utility',
        'moderation',
        'events'
    ]
    
    for cog in cogs:
        try:
            await bot.load_extension(cog)
            print(f"Loaded cog: {cog}")
        except Exception as e:
            print(f"Failed to load cog {cog}: {e}")


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)
db = Database()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await db.init_db()
    bot.start_time = discord.utils.utcnow()
    await load_cogs(bot)

@bot.command(name="help")
async def help_command(ctx):
    """Show all available commands"""
    embed = discord.Embed(
        title="🤖 Fun Bot Help",
        description="Here are all available commands:",
        color=0x0099FF
    )
    
    categories = {
        "💰 Economy": ["balance", "daily", "work", "transfer"],
        "🎮 Games": ["coinflip", "dice", "rps", "guess", "slotmachine"],
        "🎵 Music": ["play", "stop", "skip"],
        "🖼️ Images": ["meme", "cat", "dog"],
        "🔧 Utility": ["ping", "serverinfo", "userinfo", "botinfo"],
        "🛡️ Moderation": ["clear", "kick"]
    }
    
    for category, commands_list in categories.items():
        embed.add_field(
            name=category,
            value="\n".join([f"`!{cmd}`" for cmd in commands_list]),
            inline=True
        )
    
    embed.set_footer(text="Use !help <command> for more info")
    await ctx.send(embed=embed)

if __name__ == "__main__":
 bot.run("HERE")