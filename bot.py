from dotenv import load_dotenv
import requests
import json
import os

from interactions import Client, Intents, listen
from interactions import slash_command, SlashContext, slash_option, OptionType
from interactions import Status, ActivityType, Activity

from utils import bannerPrint, errorMsg, successMsg, normalMsg

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

@listen()
async def on_ready():
    successMsg(f'{client.user.display_name} is up and running.')


@slash_command(name="setserver", description="Set the BattleMetrics Server ID", scopes=[discordGuild])
@slash_option(name="serverid", description="The BattleMetrics Server ID", opt_type=OptionType.STRING, required=True)
async def setServer(ctx: SlashContext, serverid: str):
    await ctx.send(f"Server ID set to {serverid}")
    normalMsg(f"Server ID set to {serverid}")

# Start the bot
bannerPrint()
client.start()
