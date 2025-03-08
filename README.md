# 🎮 Discord Bot Setup Guide

## 📌 Introduction
This Discord bot was created for a **CS2 community server**, providing automatic role assignment and allowing users to choose their roles using reactions. However, it can be easily adapted for any other Discord server by modifying role names and descriptions.

---

## 🚀 Features
- ✅ Automatically assigns the **Member🎮** role to new users
- ✅ Allows users to choose roles (**Premier, Faceit, Play Everything**) by reacting to a message
- ✅ Provides helpful CS2-related links
- ✅ Includes basic bot commands like `!ping`, `!roles`, and `!saites`
- ✅ Keeps the bot alive using a simple Flask web server

---

## 🛠️ Requirements
Before running the bot, make sure you have:
- Python **3.8+** installed
- The following Python libraries:
  ```bash
  pip install discord.py flask
  ```
- A **Discord bot token** (explained below)

---

## 🔑 Setting Up Your Bot Token
To authenticate your bot, you need a **Discord bot token**:
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **New Application** and give it a name
3. Navigate to **Bot** → Click **Add Bot**
4. Copy the **token** and store it securely
5. Set the token as an **environment variable** on your machine:
   - **Windows (PowerShell):**
     ```powershell
     $env:DISCORD_TOKEN="your-bot-token-here"
     ```
   - **Linux/macOS:**
     ```bash
     export DISCORD_TOKEN="your-bot-token-here"
     ```

Alternatively, you can create a `.env` file and use the `dotenv` package to load it.

---

## ⚙️ Running the Bot
After setting up the bot token, you can run the bot with:
```bash
python bot.py
```

The bot will now:
- Start a **Flask web server** to keep itself alive
- Log in to Discord and display `✅ Bot is online!`
- Assign the **Member🎮** role to new users

---

## 🎭 Role Selection System
The bot allows users to pick roles by reacting to a message:
- 🟢 **Premier** – For CS2 players who play in Premier mode
- 🔵 **Faceit** – For CS2 players who play on Faceit
- 🟣 **Play Everything** – For players who enjoy all CS2 modes

When users react, the bot assigns them the corresponding role. Removing the reaction removes the role.

---

## 📜 Available Commands
| Command | Description |
|---------|-------------|
| `!ping` | 🏓 Checks if the bot is running |
| `!roles` | 🎭 Sends the role selection embed |
| `!saites` | 🔗 Provides useful CS2 links |
| `!komandas` | 📜 Lists all available commands |

---

## 🛠️ Customization
You can customize the bot by modifying:
- **Role names** (change them in the `!roles` command)
- **Reaction emojis**
- **Commands** (add new commands as needed)

If using this bot for a different server, make sure to change the **role names** and **permissions** accordingly.

---

## 🐞 Troubleshooting
### ❓ The bot doesn't respond to commands
- Make sure the bot has **Administrator** or **Manage Roles** permissions
- Check if the bot **intents** are enabled in the Discord Developer Portal

### ❓ Roles are not assigned when reacting
- Ensure that the role **names match** exactly in the script
- Check if the bot has permission to **manage roles**

### ❓ Bot is not online
- Double-check your **Discord token** setup
- Ensure all required libraries are installed

---

## 📌 Conclusion
This bot is designed to simplify role management for a CS2 community but can be modified for any Discord server. Feel free to expand its functionality by adding more commands or integrating additional features!

🎮 **Enjoy your Discord experience!** 🚀

