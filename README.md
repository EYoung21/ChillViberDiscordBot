# 🎮 Chill Viber Discord Bot

A comprehensive Discord bot system for managing democratic voting for Rust wipe participation, with automatic role assignment and exclusive channel access.

## 🌟 Features

### 🗳️ Democratic Voting System
- **Automated member listing** with voting reactions
- **Self-voting allowed** - everyone can vote for themselves
- **Real-time vote counting** from Discord reactions
- **Configurable vote threshold** (default: 3 votes to qualify)

### 🏆 Role Management
- **Automatic role creation** (`CHILL VIBER` role)
- **Vote-based role assignment** for qualified players
- **Visual role hierarchy** with custom colors and permissions

### 🔒 Exclusive Channel System
- **Private voice channels** (CHILL VIBERS 1, 2, 3)
- **Exclusive text chat** for coordination
- **Organized category structure** with proper permissions
- **Member limit controls** (10 users per voice channel)

### 📢 Announcement Management
- **Multi-channel announcements** (general, announcements, voting)
- **Automatic message editing** and updates
- **Deadline management** with countdown messaging
- **Results broadcasting** with winner celebrations

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Discord.py library
- A Discord bot token
- Server administrator permissions

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/EYoung21/ChillViberDiscordBot.git
   cd ChillViberDiscordBot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your bot token:**
   - Replace `YOUR_BOT_TOKEN_HERE` in the scripts with your actual Discord bot token
   - **⚠️ Never commit your real token to git!**

### Bot Setup in Discord

1. **Create a Discord Application:**
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a new application
   - Go to "Bot" section and create a bot user

2. **Invite Bot to Server:**
   - Use OAuth2 URL Generator with these permissions:
     - Administrator (recommended)
     - Or individually: Manage Roles, Manage Channels, Send Messages, Add Reactions

3. **Server Setup:**
   - Ensure bot role is at the top of the role hierarchy
   - Create required channels: `general`, `announcements`, `vote-for-who-plays-wipe`

## 📁 Project Structure

```
ChillViberDiscordBot/
├── README.md                              # This file
├── requirements.txt                       # Python dependencies
├── list_members.py                        # Main voting system setup
├── vote_counter_and_role_assigner.py     # Vote counting and role assignment
├── setup_chill_viber_channels.py         # Channel and role creation
├── edit_voting_messages.py               # Add nicknames to voting messages
├── voting_deadline.py                    # Deadline announcements
├── update_announcements_with_role_info.py # Update existing announcements
├── post_to_announcements.py              # Post to announcements channel
├── link_voting.py                         # Send voting channel links
├── announcement.py                        # General announcements
├── test_permissions.py                    # Bot permission diagnostics
└── run_vote_counter.bat                   # Windows batch file for scheduling
```

## 🎯 Usage Guide

### Step 1: Initial Setup
```bash
python setup_chill_viber_channels.py
```
- Creates CHILL VIBER role
- Sets up exclusive channels with permissions
- Organizes everything in a category

### Step 2: Start Voting
```bash
python list_members.py
```
- Posts voting explanation to voting channel
- Lists all server members with reaction voting
- Sends announcement to general channel

### Step 3: Manage Announcements
```bash
python voting_deadline.py           # Set voting deadline
python update_announcements_with_role_info.py  # Update with role info
python post_to_announcements.py     # Post to announcements channel
```

### Step 4: Vote Counting (Run at deadline)
```bash
python vote_counter_and_role_assigner.py
```
- Counts all votes from reactions
- Assigns CHILL VIBER role to winners (3+ votes)
- Posts results to general channel
- Grants access to exclusive channels

### Additional Utilities
```bash
python edit_voting_messages.py      # Add nicknames to existing votes
python test_permissions.py          # Check bot permissions
python link_voting.py               # Send voting channel link
```

## ⚙️ Configuration

### Vote Threshold
Edit `vote_counter_and_role_assigner.py` line 67:
```python
if votes >= 3:  # Change 3 to your desired threshold
```

### Channel Names
Update channel names in the scripts as needed:
- `general` - Main chat channel
- `announcements` - Announcements channel  
- `vote-for-who-plays-wipe` - Voting channel

### Role Customization
Modify role properties in `setup_chill_viber_channels.py`:
```python
chill_viber_role = await guild.create_role(
    name='CHILL VIBER',
    color=discord.Color.green(),  # Change color
    hoist=True,                   # Display separately
    mentionable=True              # Allow mentions
)
```

## 🕐 Scheduling

### Windows (Task Scheduler)
1. Open Task Scheduler
2. Create Basic Task
3. Set trigger for your voting deadline
4. Action: Start program → `run_vote_counter.bat`

### Linux/Mac (Cron)
```bash
# Edit crontab
crontab -e

# Add line for Thursday 2pm CST (example)
0 14 * * 4 cd /path/to/bot && python vote_counter_and_role_assigner.py
```

## 🎮 Rust Wipe Integration

This bot was specifically designed for Rust server wipe participation management:

- **Democratic server selection** - Community votes for active players
- **Organized coordination** - Private channels for strategy planning
- **Base planning support** - Channels for village, hotel, compound, oil rig coordination
- **Fair participation** - Everyone gets to vote, including for themselves

## 🛠️ Troubleshooting

### Permission Issues
```bash
python test_permissions.py  # Check bot permissions
```
**Common fixes:**
- Move bot role to top of role hierarchy
- Grant Administrator permission
- Re-invite bot with updated permissions

### Channel Not Found
- Ensure channel names match exactly (case-sensitive)
- Check for typos in channel names
- Verify bot can see the channels

### Vote Counting Issues
- Ensure bot has read message history permission
- Check that voting messages are from the correct bot
- Verify reaction format (✅ checkmark)

## 🔒 Security Notes

- **Never commit bot tokens** to version control
- Use environment variables for sensitive data
- Regularly rotate bot tokens
- Monitor bot permissions and access

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source. Feel free to modify and distribute according to your needs.

## 🎯 Future Enhancements

- [ ] Web dashboard for vote monitoring
- [ ] Multiple voting sessions support
- [ ] Vote analytics and statistics
- [ ] Integration with game servers
- [ ] Automated wipe scheduling
- [ ] Player activity tracking

---

**Made with ❤️ for the Rust community**

*For support or questions, create an issue on GitHub.* 