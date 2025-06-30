import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print(f"Setting up CHILL VIBER role and channels...")
    
    for guild in bot.guilds:
        print(f"Processing guild: {guild.name} (ID: {guild.id})")
        
        # Find or create the CHILL VIBER role
        chill_viber_role = discord.utils.get(guild.roles, name='CHILL VIBER')
        if not chill_viber_role:
            try:
                chill_viber_role = await guild.create_role(
                    name='CHILL VIBER',
                    color=discord.Color.green(),
                    reason='Role for players who got 3+ votes for wipe',
                    hoist=True,  # Display role separately in member list
                    mentionable=True  # Allow role to be mentioned
                )
                print("✅ Created CHILL VIBER role")
            except Exception as e:
                print(f"❌ Error creating CHILL VIBER role: {e}")
                continue
        else:
            print("✅ CHILL VIBER role already exists")
        
        # Get @everyone role for permission overrides
        everyone_role = guild.default_role
        
        # Channel names to create
        channel_names = ["CHILL VIBERS 1", "CHILL VIBERS 2", "CHILL VIBERS 3"]
        
        # Create category for organization (optional)
        chill_viber_category = discord.utils.get(guild.categories, name='🏆 CHILL VIBERS')
        if not chill_viber_category:
            try:
                # Set up permissions for the category
                category_overwrites = {
                    everyone_role: discord.PermissionOverwrite(
                        view_channel=False,
                        connect=False
                    ),
                    chill_viber_role: discord.PermissionOverwrite(
                        view_channel=True,
                        connect=True,
                        speak=True,
                        send_messages=True,
                        read_message_history=True
                    )
                }
                
                chill_viber_category = await guild.create_category(
                    name='🏆 CHILL VIBERS',
                    overwrites=category_overwrites,
                    reason='Category for CHILL VIBER exclusive channels'
                )
                print("✅ Created CHILL VIBERS category")
            except Exception as e:
                print(f"❌ Error creating category: {e}")
                chill_viber_category = None
        else:
            print("✅ CHILL VIBERS category already exists")
        
        # Create the three exclusive channels
        for channel_name in channel_names:
            existing_channel = discord.utils.get(guild.voice_channels, name=channel_name)
            if not existing_channel:
                try:
                    # Set up permissions for each channel
                    channel_overwrites = {
                        everyone_role: discord.PermissionOverwrite(
                            view_channel=False,
                            connect=False
                        ),
                        chill_viber_role: discord.PermissionOverwrite(
                            view_channel=True,
                            connect=True,
                            speak=True,
                            use_voice_activation=True,
                            priority_speaker=True
                        )
                    }
                    
                    new_channel = await guild.create_voice_channel(
                        name=channel_name,
                        category=chill_viber_category,
                        overwrites=channel_overwrites,
                        reason=f'Exclusive voice channel for CHILL VIBER role holders',
                        user_limit=10  # Limit to 10 users per channel
                    )
                    print(f"✅ Created voice channel: {channel_name}")
                except Exception as e:
                    print(f"❌ Error creating channel {channel_name}: {e}")
            else:
                print(f"✅ Channel {channel_name} already exists")
        
        # Also create a text channel for coordination
        text_channel_name = "chill-viber-chat"
        existing_text = discord.utils.get(guild.text_channels, name=text_channel_name)
        if not existing_text:
            try:
                text_overwrites = {
                    everyone_role: discord.PermissionOverwrite(
                        view_channel=False,
                        send_messages=False
                    ),
                    chill_viber_role: discord.PermissionOverwrite(
                        view_channel=True,
                        send_messages=True,
                        read_message_history=True,
                        embed_links=True,
                        attach_files=True,
                        use_external_emojis=True
                    )
                }
                
                text_channel = await guild.create_text_channel(
                    name=text_channel_name,
                    category=chill_viber_category,
                    overwrites=text_overwrites,
                    topic="Exclusive chat for CHILL VIBER role holders - coordinate your wipe strategies here!",
                    reason='Exclusive text channel for CHILL VIBER role holders'
                )
                print(f"✅ Created text channel: {text_channel_name}")
                
                # Send welcome message to the new text channel
                welcome_msg = """🏆 **Welcome to the CHILL VIBER exclusive area!** 🏆

🎮 **This is your private space to:**
• Coordinate wipe strategies
• Plan base builds (village, hotel, compound, oil rig!)
• Chat with other qualified players
• Share tips and tactics

🔥 **You earned this by getting 3+ votes in the democratic voting system!**

Let's make this the best Rust wipe ever! 🚀"""
                
                await text_channel.send(welcome_msg)
                print("✅ Sent welcome message to exclusive text channel")
                
            except Exception as e:
                print(f"❌ Error creating text channel: {e}")
        else:
            print(f"✅ Text channel {text_channel_name} already exists")
        
        print(f"\n🎉 CHILL VIBER setup completed for {guild.name}!")
        print("📋 Summary:")
        print("  • CHILL VIBER role created/verified")
        print("  • Category '🏆 CHILL VIBERS' created")
        print("  • 3 voice channels: CHILL VIBERS 1, 2, 3")
        print("  • 1 text channel: chill-viber-chat")
        print("  • All channels restricted to CHILL VIBER role only")
        print("  • Ready for vote counting script!")
    
    print("\n✅ All setup completed!")
    await bot.close()

bot.run("YOUR_BOT_TOKEN_HERE") 
