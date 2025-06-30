import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    
    for guild in bot.guilds:
        print(f"Checking permissions in guild: {guild.name}")
        
        # Get the bot's member object in this guild
        bot_member = guild.get_member(bot.user.id)
        if not bot_member:
            print("Bot member not found in guild")
            continue
            
        print(f"Bot's roles: {[role.name for role in bot_member.roles]}")
        print(f"Bot's top role: {bot_member.top_role.name}")
        print(f"Bot's top role position: {bot_member.top_role.position}")
        
        # Check specific permissions
        permissions = bot_member.guild_permissions
        print(f"\nBot permissions:")
        print(f"  Administrator: {permissions.administrator}")
        print(f"  Manage Roles: {permissions.manage_roles}")
        print(f"  Manage Channels: {permissions.manage_channels}")
        print(f"  Create Instant Invite: {permissions.create_instant_invite}")
        print(f"  Send Messages: {permissions.send_messages}")
        print(f"  Add Reactions: {permissions.add_reactions}")
        
        # Check if CHILL VIBER role already exists
        existing_role = discord.utils.get(guild.roles, name='CHILL VIBER')
        if existing_role:
            print(f"\nCHILL VIBER role already exists at position: {existing_role.position}")
        else:
            print(f"\nCHILL VIBER role does not exist yet")
            
        print(f"\nHighest role in server: {guild.roles[-1].name} (position: {guild.roles[-1].position})")
    
    await bot.close()

bot.run("YOUR_BOT_TOKEN_HERE") 
