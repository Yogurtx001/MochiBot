import discord
from discord.ext import commands
import random
import os
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1235176486156111954)  
    if channel:
        messages = [
            f"👋 Welcome, {member.mention}! Put your feet up 🦶, sit back 🛋️, and do all the grinding for us ⚒️💪.",
            f"🎉 Hey {member.mention}! We’ve been expecting you. Time to get to work! 💼",
            f"😄 Welcome aboard, {member.mention}! Coffee’s in the corner ☕, memes in the lounge 🎭.",
            f"🔥 {member.mention} just joined the grind train — no breaks allowed! 🚂💨",
            f"😎 Yo {member.mention}, welcome to the chill zone. Mind the rules and enjoy the vibes 🎧."
        ]
        chosen = random.choice(messages)
        await channel.send(chosen)


keep_alive()
bot.run(os.getenv("TOKEN"))