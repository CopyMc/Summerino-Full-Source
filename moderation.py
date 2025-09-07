import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="clear")
    @commands.has_permissions(manage_messages=True)
    async def clear_messages(self, ctx, amount: int = 10):
        """Clear messages from channel"""
        if amount > 100:
            amount = 100
        
        deleted = await ctx.channel.purge(limit=amount + 1)
        embed = discord.Embed(
            title="✅ Messages Cleared",
            description=f"Deleted {len(deleted) - 1} messages",
            color=0x00FF00
        )
        await ctx.send(embed=embed, delete_after=5)
    
    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def kick_member(self, ctx, member: discord.Member, *, reason: str = "No reason provided"):
        """Kick a member from the server"""
        await member.kick(reason=reason)
        embed = discord.Embed(
            title="👢 Member Kicked",
            description=f"{member.mention} has been kicked\nReason: {reason}",
            color=0xFF0000
        )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Moderation(bot))