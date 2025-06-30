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
            print(f"Could not find general channel")
            continue
            
        if not voting_channel:
            print(f"Could not find voting channel")
            continue
            
        print(f"Found channels - General: {general_channel.name}, Voting: {voting_channel.name}")

        # Update the pinned voting explanation message
        try:
            pinned_messages = await voting_channel.pins()
            voting_explanation_msg = None
            
            for message in pinned_messages:
                if message.author == bot.user and "RUST WIPE VOTING SYSTEM" in message.content:
                    voting_explanation_msg = message
                    break
            
            if voting_explanation_msg:
                # Updated voting explanation with CHILL VIBER role info
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

🏆 **WINNERS GET THE CHILL VIBER ROLE!** 🏆
• Access to exclusive CHILL VIBER channels
• Private voice chats for coordination
• Special status in the server

Good luck everyone! 🎮"""

                await voting_explanation_msg.edit(content=updated_explanation)
                print("✅ Updated pinned voting explanation with CHILL VIBER role info")
            else:
                print("❌ Could not find pinned voting explanation message")
                
        except Exception as e:
            print(f"❌ Error updating pinned message: {e}")

        # Send comprehensive CHILL VIBER role announcement
        role_announcement = """🏆 **INTRODUCING: THE CHILL VIBER ROLE SYSTEM!** 🏆

🎮 **What happens when voting ends on Thursday at 2pm?**

**WINNERS (3+ votes) GET:**
✅ **CHILL VIBER role** - Special green role that shows your elite status
✅ **Access to exclusive channels** in the 🏆 CHILL VIBERS category:
   • CHILL VIBERS 1, 2, 3 (voice channels for coordination)
   • chill-viber-chat (private text chat)
✅ **Priority coordination** for the epic wipe strategies

**WHY THIS SYSTEM ROCKS:**
🔥 **Democratic** - Community decides who plays
🔥 **Exclusive** - Only voted players get access
🔥 **Organized** - Private channels for better coordination
🔥 **Fair** - Everyone gets to vote, including for themselves

**REMEMBER THE WIPE PLANS:**
🏘️ Village base system
🏨 Hotel compound  
🏭 Compound system
🛢️ Oil rig base

**This is going to be the most organized and epic Rust wipe ever!**

🗳️ **VOTE NOW** in the voting channel - don't miss out on being part of the CHILL VIBER elite! 

The countdown has begun... ⏰"""

        try:
            await general_channel.send(role_announcement)
            print("✅ Sent comprehensive CHILL VIBER role announcement")
        except Exception as e:
            print(f"❌ Error sending role announcement: {e}")

    print("✅ Finished updating announcements with CHILL VIBER role information")
    await bot.close()

bot.run("YOUR_BOT_TOKEN_HERE") 
