import discord
from discord.ext import commands
import aiohttp
import random

class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="meme")
    async def meme(self, ctx):
        """Get a random meme"""
        async with aiohttp.ClientSession() as session:
            async with session.get('https://meme-api.com/gimme') as response:
                data = await response.json()
                
                embed = discord.Embed(
                    title=data['title'],
                    color=0xFF00FF
                )
                embed.set_image(url=data['url'])
                embed.set_footer(text=f"From r/{data['subreddit']}")
                
                await ctx.send(embed=embed)
    
    @commands.command(name="cat")
    async def cat(self, ctx):
        """Get a random cat picture"""
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.thecatapi.com/v1/images/search') as response:
                data = await response.json()
                
                embed = discord.Embed(
                    title="🐱 Random Cat",
                    color=0x0099FF
                )
                embed.set_image(url=data[0]['url'])
                
                await ctx.send(embed=embed)
    
    @commands.command(name="dog")
    async def dog(self, ctx):
        """Get a random dog picture"""
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.thedogapi.com/v1/images/search') as response:
                data = await response.json()
                
                embed = discord.Embed(
                    title="🐶 Random Dog",
                    color=0x0099FF
                )
                embed.set_image(url=data[0]['url'])
                
                await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Images(bot))