import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    for guild in bot.guilds:
        print(f"Processing guild: {guild.name} (ID: {guild.id})")
        
        voting_channel = discord.utils.get(guild.text_channels, name='vote-for-who-plays-wipe')
        
        if not voting_channel:
            print(f"Could not find a 'vote-for-who-plays-wipe' channel in {guild.name}. Skipping.")
            continue
            
        print(f"Found voting channel: {voting_channel.name}")
        
        # Get all members to create a mapping of usernames to display names
        member_map = {}
        async for member in guild.fetch_members(limit=None):
            if not member.bot:
                # Use display_name if different from username, otherwise just username
                if member.display_name != member.name:
                    member_map[member.name] = f"**{member.name}** ({member.display_name})"
                else:
                    member_map[member.name] = f"**{member.name}**"
        
        print(f"Created mapping for {len(member_map)} members")
        
        # Get messages from the voting channel (excluding pinned messages)
        messages_updated = 0
        async for message in voting_channel.history(limit=None):
            # Skip if message is from a different bot or pinned
            if message.author != bot.user or message.pinned:
                continue
            
            # Check if message content matches a member name format
            content = message.content.strip()
            if content.startswith("**") and content.endswith("**"):
                # Extract username from **username** format
                username = content[2:-2]  # Remove ** from both ends
                
                if username in member_map:
                    new_content = member_map[username]
                    if new_content != content:
                        try:
                            await message.edit(content=new_content)
                            print(f"Updated message for {username}")
                            messages_updated += 1
                        except Exception as e:
                            print(f"Error updating message for {username}: {e}")
        
        print(f"Updated {messages_updated} voting messages with nicknames")

    print("Finished updating voting messages.")
    await bot.close()

bot.run("YOUR_BOT_TOKEN_HERE") 
