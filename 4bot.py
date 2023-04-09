import discord, my_token, random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='$', intents=intents)


word_list = []


@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    

@client.command()
async def ping(ctx):
    await ctx.send('Pong')

@client.command()
async def newgame(ctx):
	print('$newgame command received')
	

	with open("words.txt", "r") as f:
		word_list = f.read().splitlines()
	word = random.choice(word_list)

	length = len(word)
	
	print(word)
	print(length)

	dashes = '-' * len(word)
	print(dashes)


	await ctx.send(f'Starting hangman game. Word is ' + str(len(word)) + ' characters long.')

@client.command()
async def endgame(ctx):
	print('$endgame command received')

	exit()


client.run(my_token.mytoken)
