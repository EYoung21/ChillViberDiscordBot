import discord
from discord.ext import commands
import asyncio
from datetime import datetime, timezone, timedelta

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print(f"Vote counting started at: {datetime.now()}")
    
    for guild in bot.guilds:
        print(f"Processing guild: {guild.name} (ID: {guild.id})")
        
        voting_channel = discord.utils.get(guild.text_channels, name='vote-for-who-plays-wipe')
        general_channel = discord.utils.get(guild.text_channels, name='general')
        
        if not voting_channel:
            print(f"Could not find voting channel in {guild.name}. Skipping.")
            continue
        
        print(f"Found voting channel: {voting_channel.name}")
        
        # Find or create the CHILL VIBER role
        chill_viber_role = discord.utils.get(guild.roles, name='CHILL VIBER')
        if not chill_viber_role:
            try:
                chill_viber_role = await guild.create_role(
                    name='CHILL VIBER',
                    color=discord.Color.green(),
                    reason='Role for players who got 3+ votes for wipe'
                )
                print("Created CHILL VIBER role")
            except Exception as e:
                print(f"Error creating CHILL VIBER role: {e}")
                continue
        
        # Dictionary to store vote counts
        vote_counts = {}
        username_to_member = {}
        
        # Get all members and create mapping
        async for member in guild.fetch_members(limit=None):
            if not member.bot:
                username_to_member[member.name] = member
        
        print(f"Processing votes from {voting_channel.name}...")
        
        # Count votes from voting messages
        async for message in voting_channel.history(limit=None):
            # Skip pinned messages and messages not from our bot
            if message.pinned or message.author != bot.user:
                continue
            
            # Check if message is a voting message (starts and ends with **)
            content = message.content.strip()
            if content.startswith("**") and ("**" in content[2:]):
                # Extract username (everything before the first closing **)
                end_pos = content.find("**", 2)
                if end_pos != -1:
                    username = content[2:end_pos]
                    
                    # Count checkmark reactions
                    checkmark_count = 0
                    for reaction in message.reactions:
                        if str(reaction.emoji) == '✅':
                            checkmark_count = reaction.count
                            # Subtract 1 if the bot reacted (initial reaction)
                            async for user in reaction.users():
                                if user == bot.user:
                                    checkmark_count -= 1
                                    break
                            break
                    
                    vote_counts[username] = checkmark_count
                    print(f"{username}: {checkmark_count} votes")
        
        print(f"\n=== VOTING RESULTS ===")
        
        # Sort by vote count (highest first)
        sorted_votes = sorted(vote_counts.items(), key=lambda x: x[1], reverse=True)
        
        winners = []
        role_assignments = 0
        
        for username, votes in sorted_votes:
            if votes >= 3:
                print(f"✅ {username}: {votes} votes - QUALIFIED")
                winners.append((username, votes))
                
                # Assign role to member
                if username in username_to_member:
                    member = username_to_member[username]
                    if chill_viber_role not in member.roles:
                        try:
                            await member.add_roles(chill_viber_role, reason=f"Got {votes} votes in wipe voting")
                            role_assignments += 1
                            print(f"  → Assigned CHILL VIBER role to {username}")
                        except Exception as e:
                            print(f"  → Error assigning role to {username}: {e}")
                    else:
                        print(f"  → {username} already has CHILL VIBER role")
            else:
                print(f"❌ {username}: {votes} votes - not qualified")
        
        # Send results to general channel
        if general_channel and winners:
            results_message = f"""🏆 **VOTING RESULTS ARE IN!** 🏆

📊 **{len(winners)} players qualified with 3+ votes:**

"""
            for username, votes in winners:
                results_message += f"• **{username}** - {votes} votes ✅\n"
            
            results_message += f"""
🎮 **Congratulations to all qualified players!**
You now have the **CHILL VIBER** role and access to the exclusive channels!

The wipe is going to be EPIC! 🔥"""
            
            try:
                await general_channel.send(results_message)
                print("Sent results announcement to general channel")
            except Exception as e:
                print(f"Error sending results: {e}")
        
        print(f"\n=== SUMMARY ===")
        print(f"Total votes processed: {len(vote_counts)}")
        print(f"Qualified players: {len(winners)}")
        print(f"Role assignments made: {role_assignments}")
    
    print("Vote counting and role assignment completed!")
    await bot.close()

# Note: To run this automatically at 2pm CST on June 3rd, you would typically use a task scheduler
# For Windows: Use Task Scheduler
# For Linux/Mac: Use cron jobs
# This script can also be run manually at the specified time

bot.run("YOUR_BOT_TOKEN_HERE") 
