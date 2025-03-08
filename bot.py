import discord
from discord.ext import commands
import os
import threading
from flask import Flask

# Create a simple web server using Flask to keep the bot alive
app = Flask(__name__)

@app.route('/')
def home():
    return "Discord bot is running!"

# Function to run the web server on port 8080
def run_server():
    app.run(host='0.0.0.0', port=8080)

# Retrieve the bot token from environment variables (must be set up beforehand)
TOKEN = os.environ.get("DISCORD_TOKEN")

# Set up bot intents
intents = discord.Intents.default()
intents.members = True  # Allows tracking when members join the server
intents.message_content = True  # Allows reading messages

# Create the bot instance with command prefix '!'
bot = commands.Bot(command_prefix="!", intents=intents)

# Event triggered when the bot successfully logs in and is ready
@bot.event
async def on_ready():
    print(f'✅ Bot {bot.user} is online!')

# Event triggered when a new member joins the server
@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="Member🎮")  # Find the "Member🎮" role
    if role:
        await member.add_roles(role)  # Assign the role to the new member
        print(f'🔹 Assigned role {role.name} to {member.name}')

# Command to check if the bot is responsive
@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong! I'm working!")

# Command to send an embed with role selection options
@bot.command()
async def roles(ctx):
    embed = discord.Embed(title="Choose Your Role!", color=discord.Color.blue())
    embed.add_field(name="🟢 Premier", value="For players who play CS2 Premier mode", inline=False)
    embed.add_field(name="🔵 Faceit", value="For players who play on Faceit", inline=False)
    embed.add_field(name="🟣 Play Everything", value="For players who enjoy all CS2 modes", inline=False)
    message = await ctx.send(embed=embed)
    
    # Add reactions for role selection
    await message.add_reaction("🟢")  # Premier
    await message.add_reaction("🔵")  # Faceit
    await message.add_reaction("🟣")  # Play Everything
    
    # Save message ID to a file to track reactions
    with open("roles_reaction_message.txt", "w") as file:
        file.write(str(message.id))

# Event triggered when a user adds a reaction to a message
@bot.event
async def on_raw_reaction_add(payload):
    guild = discord.utils.get(bot.guilds, id=payload.guild_id)
    if not guild:
        return
    
    member = discord.utils.get(guild.members, id=payload.user_id)
    if not member or member.bot:
        return  # Ignore bot reactions
    
    # Load the role selection message ID
    with open("roles_reaction_message.txt", "r") as file:
        role_message_id = int(file.read().strip())
    
    if payload.message_id != role_message_id:
        return  # Ignore reactions on other messages
    
    # Match reaction to role
    role_name = None
    if payload.emoji.name == "🟢":
        role_name = "Premier"
    elif payload.emoji.name == "🔵":
        role_name = "Faceit"
    elif payload.emoji.name == "🟣":
        role_name = "Play Everything"
    
    if role_name:
        role = discord.utils.get(guild.roles, name=role_name)
        if role:
            await member.add_roles(role)  # Assign the role

# Event triggered when a user removes a reaction from a message
@bot.event
async def on_raw_reaction_remove(payload):
    guild = discord.utils.get(bot.guilds, id=payload.guild_id)
    if not guild:
        return
    
    member = discord.utils.get(guild.members, id=payload.user_id)
    if not member:
        return
    
    # Load the role selection message ID
    with open("roles_reaction_message.txt", "r") as file:
        role_message_id = int(file.read().strip())
    
    if payload.message_id != role_message_id:
        return
    
    # Match reaction to role
    role_name = None
    if payload.emoji.name == "🟢":
        role_name = "Premier"
    elif payload.emoji.name == "🔵":
        role_name = "Faceit"
    elif payload.emoji.name == "🟣":
        role_name = "Play Everything"
    
    if role_name:
        role = discord.utils.get(guild.roles, name=role_name)
        if role:
            await member.remove_roles(role)  # Remove the role

# Run the Flask web server in a separate thread
server_thread = threading.Thread(target=run_server)
server_thread.start()

# Start the bot using the provided token
bot.run(TOKEN)
