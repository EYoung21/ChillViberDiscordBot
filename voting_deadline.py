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
        voting_channel = discord.utils.get(guild.text_channels, name='vote-for-who-plays-wipe')
        
        if not general_channel:
            print(f"Could not find a 'general' channel in {guild.name}. Skipping.")
            continue
            
        if not voting_channel:
            print(f"Could not find a 'vote-for-who-plays-wipe' channel in {guild.name}. Skipping.")
            continue
            
        print(f"Found channels - General: {general_channel.name}, Voting: {voting_channel.name}")

        # Send voting deadline announcement to general
        deadline_announcement = """⏰ **VOTING DEADLINE ANNOUNCED!** ⏰

🗳️ **Voting will END at 2pm on Thursday, June 3rd** 🗳️

⚠️ **This is your final chance to vote!** 
Don't miss out on the epic wipe - make sure you vote before the deadline!

Get your votes in NOW! 🏃‍♂️💨"""

        try:
            await general_channel.send(deadline_announcement)
            print("Sent voting deadline announcement in general channel.")
        except Exception as e:
            print(f"Error sending deadline announcement: {e}")

        # Find and edit the pinned voting explanation message
        try:
            pinned_messages = await voting_channel.pins()
            voting_explanation_msg = None
            
            for message in pinned_messages:
                if message.author == bot.user and "RUST WIPE VOTING SYSTEM" in message.content:
                    voting_explanation_msg = message
                    break
            
            if voting_explanation_msg:
                # Updated voting explanation with deadline
                updated_explanation = """🗳️ **RUST WIPE VOTING SYSTEM** 🗳️

THIS IS A VOTING SYSTEM FOR WHO WILL PLAY NEXT WIPE.

**How it works:**
• Everyone starts with one vote
• You can vote for yourself or others
• React with ✅ to vote for someone
• Those with at least 3 votes will get to play next wipe

**Rules:**
• Be fair and vote for active/committed players
• You can change your vote by unreacting and reacting to someone else

⏰ **VOTING DEADLINE: 2pm on Thursday, June 3rd** ⏰

Good luck everyone! 🎮"""

                await voting_explanation_msg.edit(content=updated_explanation)
                print("Updated pinned voting explanation message with deadline.")
            else:
                print("Could not find the pinned voting explanation message to update.")
                
        except Exception as e:
            print(f"Error updating pinned message: {e}")

    print("Finished updating voting deadline information.")
    await bot.close()

bot.run("YOUR_BOT_TOKEN_HERE") 
