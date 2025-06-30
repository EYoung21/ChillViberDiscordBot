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

        # Send the voting channel link
        voting_link_message = f"🗳️ **VOTE HERE:** {voting_channel.mention} 👈 Click to go vote!"

        try:
            await general_channel.send(voting_link_message)
            print("Sent voting channel link in general channel.")
        except Exception as e:
            print(f"Error sending voting link: {e}")

    print("Finished sending voting channel link.")
    await bot.close()

bot.run("YOUR_BOT_TOKEN_HERE") 
