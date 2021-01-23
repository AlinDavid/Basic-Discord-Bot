import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import requests
import json
import urllib
import re

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix="$")

def get_quote():

	response = requests.get('https://zenquotes.io/api/random')
	json_data = json.loads(response.text)
	quote = json_data[0]['q'] + ' -' + json_data[0]['a']

	return quote


@bot.event
async def on_message(message):
	if message.content == "$inspire":
		quote = get_quote()
		await message.channel.send(quote)

	await bot.process_commands(message)

@bot.command(
	help="Uses come crazy logic to determine if pong is actually the correct value or not.",
	brief="Prints pong back to the channel."
)
async def ping(ctx):
	await ctx.channel.send("pong")

@bot.command(
	help="Looks like you need some help.",
	brief="Prints the list of values back to the channel."
)
async def print(ctx, *args):
	response = "lasa ma in pace"

	for arg in args:
		response = response + " " + arg

	await ctx.channel.send(response)


@commands.command()
async def yt(self, ctx, *, search):

	query_string = urllib.parse.urlencode({'search_query': search})
	htm_content = urllib.request.urlopen('http://www.youtube.com/results?' + query_string)
	search_results = re.findall(r'/watch\?v=(.{11})',htm_content.read().decode())

	await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])

bot.run('ODAyMjY2NzY2MTM4MDE1NzQ1.YAsvJg.NxFIqopZ00ZJAtXVPS6spdJlNPQ') - # My TOKEN Bot in my case
