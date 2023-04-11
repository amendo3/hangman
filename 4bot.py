import discord, my_token, random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='$', intents=intents)


word_list = []
HANGMAN_PICS = [r'''
   +---+
   |
   |
   |
   ===
   ''', r'''
   +---+
   |   O
   |
   |
   ===
   ''', r'''
   +---+
   |   O
   |   |
   |
   ===
   ''', r'''
   +---+
   |   O
   |  /|
   |
   ===
   ''', r'''
   +---+
   |   O
   |  /|\
   |
   ===
   ''', r'''
   +---+
   |   O
   |  /|\
   |  /
   ===
   ''', r'''
   +---+
   |   O
   |  /|\
   |  / \
   ===    ''']



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
	word = random.choice(word_list) # selectWord
	correct_word_list = list(word) # word_list

	length = len(word)
	
	print(correct_word_list)
	print(word)
	print(length)

	dashes = '-' * len(word) # blanks
	dashes_list = list(dashes) # blanks list
	another_dashes_list = list(dashes) # new blanks list
	guess_list = []

	print(dashes)


	
	guesses = 0

	async def print_hangman(guesses):
		if (guesses == 0):
			print(HANGMAN_PICS[0])
			await ctx.send(HANGMAN_PICS[0])
		elif (guesses == 1):
			print(HANGMAN_PICS[1])
			await ctx.send(HANGMAN_PICS[1])
		elif (guesses == 2):
			print(HANGMAN_PICS[2])
			await ctx.send(HANGMAN_PICS[2])
		elif (guesses == 3):
			print(HANGMAN_PICS[3])
			await ctx.send(HANGMAN_PICS[3])
		elif (guesses == 4):
			print(HANGMAN_PICS[4])
			await ctx.send(HANGMAN_PICS[4])
		elif (guesses == 5):
			print(HANGMAN_PICS[5])
			await ctx.send(HANGMAN_PICS[5])
		elif (guesses == 6):
			print(HANGMAN_PICS[6])
			await ctx.send(HANGMAN_PICS[6])

	await ctx.send(f'Starting hangman game. Word is ' + str(len(word)) + ' characters long.')
	await print_hangman(guesses)

	

	while guesses < 6:
		guess2 = await client.wait_for("message")
		guess1 = guess2.content
		print(guess1)

		if len(guess1) > 1:
			print('That is more than 1 character.')
			await ctx.send(f'That is more than 1 character.')
		elif guess1 == '':
			print('That is a blank space.')
			await ctx.send(f'That is a blank space.')
		elif guess1 in guess_list:
			('You already tried that letter! So far you guessed: ' + ''.join(guess_list))
			await ctx.send(f'You already tried that letter! So far you guessed: ' + ''.join(guess_list))
		else:
			guess_list.append(guess1)
			i = 0
			while i < len(word):
				if guess1 == word[i]:
					another_dashes_list[i] = correct_word_list[i]
				i += 1

			if another_dashes_list == dashes_list:
				print('Your letter is not here.')
				await ctx.send('Your letter is not here.')
				guesses += 1
				await print_hangman(guesses)

				if guesses < 6:
					print('Guess again.' + ''.join(dashes_list))
					await ctx.send('Guess again.' + ''.join(dashes_list))

			elif correct_word_list != dashes_list:
				dashes_list = another_dashes_list[:]
				print(','.join(dashes_list))
				await ctx.send(','.join(dashes_list))

				if correct_word_list == dashes_list:
					print('You win! The word was ' + word)
					await ctx.send(r"You win! The word was " + word)

				else:
					print('Good guess! Go again.')
					await ctx.send(r'Good guess! Go again.')
	
	

@client.command()
async def endgame(ctx):
	print('$endgame command received')

	exit()


client.run(my_token.mytoken)
