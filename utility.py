import discord
from discord.ext import commands
import datetime
import platform

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="ping")
    async def ping(self, ctx):
        """Check bot's latency"""
        latency = round(self.bot.latency * 1000)
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"Latency: {latency}ms",
            color=0x00FF00
        )
        await ctx.send(embed=embed)
    
    @commands.command(name="serverinfo")
    async def server_info(self, ctx):
        """Display server information"""
        guild = ctx.guild
        embed = discord.Embed(
            title=f"📊 {guild.name} Info",
            color=0x0099FF
        )
        embed.add_field(name="Members", value=guild.member_count, inline=True)
        embed.add_field(name="Channels", value=len(guild.channels), inline=True)
        embed.add_field(name="Roles", value=len(guild.roles), inline=True)
        embed.add_field(name="Created", value=guild.created_at.strftime("%Y-%m-%d"), inline=True)
        embed.add_field(name="Owner", value=guild.owner.mention, inline=True)
        embed.set_thumbnail(url=guild.icon.url)
        
        await ctx.send(embed=embed)
    
    @commands.command(name="userinfo")
    async def user_info(self, ctx, member: discord.Member = None):
        """Display user information"""
        member = member or ctx.author
        embed = discord.Embed(
            title=f"👤 {member.name}'s Info",
            color=0x0099FF
        )
        embed.add_field(name="ID", value=member.id, inline=True)
        embed.add_field(name="Joined", value=member.joined_at.strftime("%Y-%m-%d"), inline=True)
        embed.add_field(name="Account Created", value=member.created_at.strftime("%Y-%m-%d"), inline=True)
        embed.add_field(name="Roles", value=len(member.roles) - 1, inline=True)
        embed.set_thumbnail(url=member.avatar.url)
        
        await ctx.send(embed=embed)
    
    @commands.command(name="botinfo")
    async def bot_info(self, ctx):
        """Display bot information"""
        embed = discord.Embed(
            title="🤖 Bot Information",
            color=0x0099FF
        )
        embed.add_field(name="Python Version", value=platform.python_version(), inline=True)
        embed.add_field(name="Discord.py Version", value=discord.__version__, inline=True)
        embed.add_field(name="Servers", value=len(self.bot.guilds), inline=True)
        embed.add_field(name="Users", value=len(self.bot.users), inline=True)
        embed.add_field(name="Uptime", value=str(datetime.datetime.now() - self.bot.start_time), inline=True)
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Utility(bot))