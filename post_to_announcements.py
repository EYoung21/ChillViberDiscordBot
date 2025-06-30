import discord
from discord.ext import commands

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    
    for guild in bot.guilds:
        print(f"Processing guild: {guild.name} (ID: {guild.id})")
        
        # Look for announcements channel
        announcements_channel = discord.utils.get(guild.text_channels, name='announcements')
        
        if not announcements_channel:
            print(f"Could not find announcements channel")
            continue
            
        print(f"Found announcements channel: {announcements_channel.name}")

        # Send comprehensive CHILL VIBER role announcement to announcements
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
            announcement_msg = await announcements_channel.send(role_announcement)
            # Try to publish the announcement if it's in an announcement channel
            try:
                await announcement_msg.publish()
                print("✅ Sent and published CHILL VIBER role announcement")
            except:
                print("✅ Sent CHILL VIBER role announcement (couldn't publish - may not be news channel)")
        except Exception as e:
            print(f"❌ Error sending announcement: {e}")

    print("✅ Finished posting to announcements channel")
    await bot.close()

bot.run("YOUR_BOT_TOKEN_HERE") 
