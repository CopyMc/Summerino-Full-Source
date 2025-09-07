import discord
from discord.ext import commands
import random
import datetime
from database import db
from config import STARTING_BALANCE, DAILY_REWARD, WORK_REWARD_MIN, WORK_REWARD_MAX

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="balance", aliases=["bal", "money"])
    async def balance(self, ctx, member: discord.Member = None):
        """Check your balance"""
        member = member or ctx.author
        result = await db.get_balance(member.id)
        
        if result:
            balance, bank = result
            embed = discord.Embed(
                title=f"💰 {member.name}'s Balance",
                color=0x00FF00
            )
            embed.add_field(name="Cash", value=f"${balance}", inline=True)
            embed.add_field(name="Bank", value=f"${bank}", inline=True)
            embed.add_field(name="Total", value=f"${balance + bank}", inline=True)
        else:
            embed = discord.Embed(
                title="❌ Error",
                description="User not found in database",
                color=0xFF0000
            )
        
        await ctx.send(embed=embed)
    
    @commands.command(name="daily")
    async def daily(self, ctx):


        reward = DAILY_REWARD
        await db.update_balance(ctx.author.id, reward)
        
        embed = discord.Embed(
            title="🎉 Daily Reward",
            description=f"You received ${reward}!",
            color=0x00FF00
        )
        await ctx.send(embed=embed)
    
    @commands.command(name="work")
    async def work(self, ctx):

        reward = random.randint(WORK_REWARD_MIN, WORK_REWARD_MAX)
        await db.update_balance(ctx.author.id, reward)
        
        embed = discord.Embed(
            title="💼 Work Completed",
            description=f"You earned ${reward} from working!",
            color=0x00FF00
        )
        await ctx.send(embed=embed)
    
    @commands.command(name="transfer", aliases=["pay"])
    async def transfer(self, ctx, member: discord.Member, amount: int):

        if amount <= 0:
            await ctx.send("Amount must be positive!")
            return
        
        await db.transfer_money(ctx.author.id, member.id, amount)
        
        embed = discord.Embed(
            title="✅ Transfer Successful",
            description=f"Transferred ${amount} to {member.mention}",
            color=0x00FF00
        )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Economy(bot))