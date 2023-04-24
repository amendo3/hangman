import discord, my_token, random
from discord.ext import commands

# intents statements required for discord api, I have default here but have also seen Intents.all()
# can look more into this later to see other options
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='$', intents=intents)

# global variables
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


# Bot logs into server
@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    

# First command I figured out (copied), on $ping sends pong
@client.command()
async def ping(ctx):
    await ctx.send('Pong')

# creating our hangman game, $newgame to begin it. $endgame currently closes bot rather than change game state to off
@client.command()
async def newgame(ctx):

	if ctx.author.id == client.user.id:
		print('author id error thingy')
		return

	print('$newgame command received')
	
	# get random word from the file of 500. assign to variable and assign a list of the letters
	with open("words.txt", "r") as f:
		word_list = f.read().splitlines()
	word = random.choice(word_list) # selectWord
	correct_word_list = list(word) # word_list

	length = len(word)
	
	# console check statements
	print(correct_word_list)
	print(word)
	print(length)

	# set up lists for visualizing guesses and which spot had the letter(s)
	dashes = '-' * len(word) # blanks
	dashes_list = list(dashes) # blanks list
	another_dashes_list = list(dashes) # new blanks list
	guess_list = []

	print(dashes)
	
	# set guesses to 0 as the game starts
	guesses = 0

	# function for printing out hangman visual at different game states
	async def print_hangman(guesses):
		if (guesses == 0):
			print(str(guesses) + ' wrong guesses.' + HANGMAN_PICS[0])
			await ctx.send(str(guesses) + ' wrong guesses.' + HANGMAN_PICS[0])
		elif (guesses == 1):
			print(str(guesses) + ' wrong guess.' + HANGMAN_PICS[1])
			await ctx.send(str(guesses) + ' wrong guess.' + HANGMAN_PICS[1])
		elif (guesses == 2):
			print(str(guesses) + ' wrong guesses.' + HANGMAN_PICS[2])
			await ctx.send(str(guesses) + ' wrong guesses.' + HANGMAN_PICS[2])
		elif (guesses == 3):
			print(str(guesses) + ' wrong guesses.' + HANGMAN_PICS[3])
			await ctx.send(str(guesses) + ' wrong guesses.' + HANGMAN_PICS[3])
		elif (guesses == 4):
			print(str(guesses) + ' wrong guesses.' + HANGMAN_PICS[4])
			await ctx.send(str(guesses) + ' wrong guesses.' + HANGMAN_PICS[4])
		elif (guesses == 5):
			print(str(guesses) + ' wrong guesses.' + HANGMAN_PICS[5])
			await ctx.send(str(guesses) + ' wrong guesses.' + HANGMAN_PICS[5])
		elif (guesses == 6):
			print(str(guesses) + ' wrong guesses.' + HANGMAN_PICS[6])
			await ctx.send(str(guesses) + ' wrong guesses.' + HANGMAN_PICS[6])

	# first messages from the bot to the server
	await ctx.send(f'~-~- HANGMAN STARTED -~-~ \n The word is ' + str(len(word)) + ' characters long.')
	await print_hangman(guesses)

	

	while guesses < 6:
		# get info from the discord user, assign it to values to manipulate
		guess2 = await client.wait_for("message")
		guess1 = guess2.content

		print(guess1)

		
		if ctx.author.id == client.user.id:
			pass
		elif len(guess1) > 1: # seems to work perfectly fine
			print('That is more than 1 character.')
			await ctx.send(f'That is more than 1 character.')
		elif guess1.isalpha() == False:
			print('Letters only!')
			await ctx.send(f'Letters only!')
		elif guess1 == '':
			print('That is a blank space.') # not sure if this is needed, discord client doesn't seem to allow a message with only a space
			await ctx.send(f'That is a blank space.')
		elif guess1 in guess_list: 
			('You already tried that letter! So far you guessed: ' + ', '.join(guess_list))
			await ctx.send(f'You already tried that letter! So far you guessed: ' + ', '.join(guess_list))
		else:
			guess_list.append(guess1)
			print(guess_list) # console check statement
			i = 0
			while i < len(word):
				if guess1 == word[i]:
					another_dashes_list[i] = correct_word_list[i]
				i += 1

			if another_dashes_list == dashes_list:
				print('That letter is not in the word. Already used: ' + ' '.join(guess_list))
				await ctx.send('That letter is not in the word. Already used: ' + ' '.join(guess_list))
				guesses += 1
				print(guesses) # console check statement
				await print_hangman(guesses)

				if guesses < 6:
					print('Guess again. Here is your word progress:    ' + ' '.join(dashes_list))
					await ctx.send('Guess again. Here is your word progress:    ' + ' '.join(dashes_list))

			elif correct_word_list != dashes_list:
				dashes_list = another_dashes_list[:]
				print(' '.join(dashes_list))
				await ctx.send(' '.join(dashes_list))

				if correct_word_list == dashes_list:
					print('You win! The word was ' + word)
					await ctx.send(r"You win! The word was " + word)

				else:
					print('Good guess! Keep going.')
					await ctx.send(r'Good guess! Keep going.')

	else:
		print('Game is over. You died!')
		await ctx.send(r'Game is over. You died!')
	

@client.command()
async def endgame(ctx):
	print('$endgame command received')

	exit()


client.run(my_token.mytoken)
