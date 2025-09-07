import aiosqlite
import datetime
import random

class Database:
    def __init__(self):
        self.db_path = "funbot.db"
    
    async def init_db(self):
        async with aiosqlite.connect(self.db_path) as db:

            await db.execute('''
                CREATE TABLE IF NOT EXISTS economy (
                    user_id INTEGER PRIMARY KEY,
                    balance INTEGER DEFAULT 1000,
                    bank INTEGER DEFAULT 0,
                    daily_streak INTEGER DEFAULT 0,
                    last_daily TIMESTAMP,
                    last_work TIMESTAMP
                )
            ''')
            

            await db.execute('''
                CREATE TABLE IF NOT EXISTS user_stats (
                    user_id INTEGER PRIMARY KEY,
                    messages_sent INTEGER DEFAULT 0,
                    commands_used INTEGER DEFAULT 0,
                    games_played INTEGER DEFAULT 0
                )
            ''')
            
            await db.commit()
    

    async def get_balance(self, user_id: int):
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute(
                "SELECT balance, bank FROM economy WHERE user_id = ?",
                (user_id,)
            )
            return await cursor.fetchone()
    
    async def update_balance(self, user_id: int, amount: int):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                "INSERT OR IGNORE INTO economy (user_id, balance) VALUES (?, ?)",
                (user_id, 1000)
            )
            await db.execute(
                "UPDATE economy SET balance = balance + ? WHERE user_id = ?",
                (amount, user_id)
            )
            await db.commit()
    
    async def transfer_money(self, from_id: int, to_id: int, amount: int):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                "UPDATE economy SET balance = balance - ? WHERE user_id = ? AND balance >= ?",
                (amount, from_id, amount)
            )
            await db.execute(
                "INSERT OR IGNORE INTO economy (user_id, balance) VALUES (?, ?)",
                (to_id, 1000)
            )
            await db.execute(
                "UPDATE economy SET balance = balance + ? WHERE user_id = ?",
                (amount, to_id)
            )
            await db.commit()

db = Database()