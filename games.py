import discord
from discord.ext import commands
import random
import asyncio

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="coinflip", aliases=["flip"])
    async def coinflip(self, ctx, choice: str = None):
        """Flip a coin - heads or tails"""
        result = random.choice(["heads", "tails"])
        
        if choice and choice.lower() in ["heads", "tails"]:
            if choice.lower() == result:
                outcome = "🎉 You won!"
            else:
                outcome = "😢 You lost!"
        else:
            outcome = ""
        
        embed = discord.Embed(
            title="🎲 Coin Flip",
            description=f"The coin landed on **{result}**! {outcome}",
            color=0xFFD700
        )
        await ctx.send(embed=embed)
    
    @commands.command(name="dice", aliases=["roll"])
    async def dice(self, ctx, sides: int = 6):
        """Roll a dice"""
        if sides < 2:
            sides = 6
        
        result = random.randint(1, sides)
        embed = discord.Embed(
            title="🎲 Dice Roll",
            description=f"You rolled a **{result}** on a {sides}-sided die!",
            color=0xFFD700
        )
        await ctx.send(embed=embed)
    
    @commands.command(name="rps", aliases=["rockpaperscissors"])
    async def rps(self, ctx, choice: str):
        """Play Rock Paper Scissors"""
        choices = ["rock", "paper", "scissors"]
        bot_choice = random.choice(choices)
        
        if choice.lower() not in choices:
            await ctx.send("Please choose rock, paper, or scissors!")
            return
        
        if choice.lower() == bot_choice:
            result = "It's a tie! 🤝"
        elif (choice.lower() == "rock" and bot_choice == "scissors") or \
             (choice.lower() == "paper" and bot_choice == "rock") or \
             (choice.lower() == "scissors" and bot_choice == "paper"):
            result = "You win! 🎉"
        else:
            result = "I win! 😎"
        
        embed = discord.Embed(
            title="✂️ Rock Paper Scissors",
            description=f"You chose **{choice}**\nI chose **{bot_choice}**\n\n{result}",
            color=0xFF00FF
        )
        await ctx.send(embed=embed)
    
    @commands.command(name="guess")
    async def guess_number(self, ctx, number: int):
        """Guess a number between 1-10"""
        secret = random.randint(1, 10)
        
        if number == secret:
            result = "🎉 Correct! You guessed it!"
        else:
            result = f"😢 Wrong! The number was {secret}"
        
        embed = discord.Embed(
            title="🔢 Number Guessing Game",
            description=result,
            color=0xFF00FF
        )
        await ctx.send(embed=embed)
    
    @commands.command(name="slotmachine", aliases=["slots"])
    async def slot_machine(self, ctx):
        """Play the slot machine"""
        symbols = ["🍒", "🍋", "🍊", "🍇", "🔔", "💎", "7️⃣"]
        slots = [random.choice(symbols) for _ in range(3)]
        
        if slots[0] == slots[1] == slots[2]:
            result = "🎉 JACKPOT! All symbols match!"
        elif slots[0] == slots[1] or slots[1] == slots[2]:
            result = "👍 Two symbols match! Good job!"
        else:
            result = "😢 No matches. Try again!"
        
        embed = discord.Embed(
            title="🎰 Slot Machine",
            description=f"[ {slots[0]} | {slots[1]} | {slots[2]} ]\n\n{result}",
            color=0xFF0000
        )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Games(bot))