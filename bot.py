from dotenv import load_dotenv
import requests
import json
import os

from mongoengine import connect


from interactions import Client, Intents, listen
from interactions import slash_command, SlashContext, slash_option, OptionType
from interactions import Status, ActivityType, Activity

from utils import bannerPrint, errorMsg, successMsg, normalMsg
from models import Server, Team

# Load environment variables
load_dotenv()

discordToken = os.getenv('DISCORD_BOT_TOKEN')
discordGuild = os.getenv('DISCORD_GUILD_ID')
botChannel = os.getenv('DISCORD_CHANNEL_ID')
mongoDBUri = os.getenv('MONGODB_URI')

# Create a client
client = Client(
    intents=Intents.ALL,
    token=discordToken,
    status=Status.ONLINE,
    activity=Activity(name="the enemies!", type=ActivityType.WATCHING)
)

# Connect to MongoDB
connect(host=mongoDBUri)

@listen()
async def on_ready():
    successMsg(f'{client.user.display_name} is up and running.')


@slash_command(name="addserver", description="Add a new server which is monitored", scopes=[discordGuild])
@slash_option(name="name", description="The name of the server", opt_type=OptionType.STRING, required=True)
async def setServer(ctx: SlashContext, name: str):
    
    server = Server(name=name)
    server.save()
    
    await ctx.send(f"Successfully created new server with name: {name}")
    normalMsg(f"Successfully created a new server with name: {name}")

@slash_command(name="removeserver", description="Remove a server which is monitored", scopes=[discordGuild])
@slash_option(name="name", description="The name of the server", opt_type=OptionType.STRING, required=True)
async def setServer(ctx: SlashContext, name: str):
    await ctx.defer()
    try:
        server = Server.objects(name=name).first()
        server.delete()
        
        await ctx.send(f"Successfully deleted server with name: {name}")
        normalMsg(f"Successfully deleted server with name: {name}")
    except Exception as e:
        await ctx.send(f"Error deleting server with name: {name}")
        errorMsg(f"Error deleting server with name: {name}")
        print(e)

# Start the bot
bannerPrint()
client.start()
