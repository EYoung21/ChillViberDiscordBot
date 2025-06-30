import discord
from discord.ext import commands

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    for guild in bot.guilds:
        print(f"Processing guild: {guild.name} (ID: {guild.id})")
        
        general_channel = discord.utils.get(guild.text_channels, name='general')
        
        if not general_channel:
            print(f"Could not find a 'general' channel in {guild.name}. Skipping.")
            continue
            
        print(f"Found general channel: {general_channel.name}")

        # Send the wipe announcement message
        wipe_announcement = """🏗️ **NEXT WIPE PLANS ANNOUNCED!** 🏗️

🎯 **We're doing something EPIC next wipe:**
• 🏘️ **Village base system**
• 🏨 **Hotel compound**  
• 🏭 **Compound system**
• 🛢️ **Oil rig base**

This is going to be **AMAZING** and a lot of fun! 🔥

🗳️ **Make sure to go vote in the voting channel** - you don't want to miss out on this wipe! 

Let's make this the best wipe yet! 🎮⚡"""

        try:
            await general_channel.send(wipe_announcement)
            print("Sent wipe announcement in general channel.")
        except Exception as e:
            print(f"Error sending announcement: {e}")

    print("Finished sending wipe announcement.")
    await bot.close()

bot.run("YOUR_BOT_TOKEN_HERE") 
