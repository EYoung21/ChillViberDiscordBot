import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.members = True

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

        # Send announcement in general channel
        announcement = f"""📢 **ANNOUNCEMENT** 📢

🗳️ **NEW VOTING CHANNEL CREATED!** 🗳️

Head over to {voting_channel.mention} to participate in the **RUST WIPE VOTING SYSTEM**!

This is where we'll decide who gets to play in the next wipe. Check it out now! 🎮"""

        try:
            await general_channel.send(announcement)
            print("Sent announcement in general channel.")
            await asyncio.sleep(3)
        except Exception as e:
            print(f"Error sending announcement: {e}")

        # Send the voting system explanation message in voting channel
        voting_explanation = """🗳️ **RUST WIPE VOTING SYSTEM** 🗳️

THIS IS A VOTING SYSTEM FOR WHO WILL PLAY NEXT WIPE.

**How it works:**
• Everyone starts with one vote
• You can vote for yourself or others
• React with ✅ to vote for someone
• Those with at least 3 votes will get to play next wipe

**Rules:**
• Be fair and vote for active/committed players
• You can change your vote by unreacting and reacting to someone else
• Voting closes when admin decides

Good luck everyone! 🎮"""

        try:
            explanation_msg = await voting_channel.send(voting_explanation)
            await explanation_msg.pin()
            print("Sent and pinned voting explanation message in voting channel.")
            await asyncio.sleep(2)
        except Exception as e:
            print(f"Error sending explanation message: {e}")

        excluded_bots = ["listofnames", "ProBot", "RustWipeVoting"]
        
        async for member in guild.fetch_members(limit=None):
            if member.name in excluded_bots or member.bot:
                print(f"Skipping excluded member/bot: {member.name}")
                continue
            
            try:
                message = await voting_channel.send(f"**{member.name}**")
                await message.add_reaction('✅')
                print(f"Sent voting message for {member.name} and added checkmark.")
                await asyncio.sleep(1) 
            except discord.Forbidden:
                print(f"Missing permissions to send message or react in {voting_channel.name}.")
                break
            except Exception as e:
                print(f"An error occurred while processing {member.name}: {e}")

    print("Finished setting up Rust wipe voting system.")
    await bot.close()

bot.run("YOUR_BOT_TOKEN_HERE") 
