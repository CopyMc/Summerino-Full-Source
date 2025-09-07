import discord
from discord.ext import commands
from database import db

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user} is ready!')
        await self.bot.change_presence(activity=discord.Game(name="!help for commands"))
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.text_channels, name="general")
        if channel:
            embed = discord.Embed(
                title="🎉 Welcome!",
                description=f"Welcome {member.mention} to {member.guild.name}!",
                color=0x00FF00
            )
            await channel.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_command(self, ctx):
   
        pass

async def setup(bot):
    await bot.add_cog(Events(bot))