import discord
from discord.ext import commands
import yt_dlp
import asyncio


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.queues = {}
    
    @commands.command(name="play")
    async def play_music(self, ctx, *, query: str):
        """Play music from YouTube"""

        embed = discord.Embed(
            title="🎵 Music Player",
            description=f"Searching for: {query}",
            color=0x0099FF
        )
        await ctx.send(embed=embed)
    
    @commands.command(name="stop")
    async def stop_music(self, ctx):
        """Stop the music"""
        embed = discord.Embed(
            title="⏹️ Music Stopped",
            description="Playback has been stopped",
            color=0xFF0000
        )
        await ctx.send(embed=embed)
    
    @commands.command(name="skip")
    async def skip_music(self, ctx):
        """Skip the current song"""
        embed = discord.Embed(
            title="⏭️ Song Skipped",
            description="Skipped to the next song",
            color=0x00FF00
        )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Music(bot))