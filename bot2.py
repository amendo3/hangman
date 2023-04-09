import discord
import random

# intent statements for accessing discord api
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


# variable declarations
guesses = 6
word_list = []
word = ''
game_running = False
# missedLetters = ''
# correctLetters = ''
# letter = ''
# letters_guessed = []

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

# function declarations


# def displayBoard(missedLetters, correctLetters, secretWord):
#     print(HANGMAN_PICS[len(missedLetters)])
#     print()

#     print('Missed letters:', end=' ')
#     for letter in missedLetters:
#         print(letter, end=' ')
#     print()

#     blanks = '_' * len(secretWord)

#     for i in range(len(secretWord)):  # Replace blanks with correctly guessed letters.
#         if secretWord[i] in correctLetters:
#             blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

#     for letter in blanks:  # Show secret word with spaces in btwn each letter
#         print(letter, end=' ')
#     print()


# def getGuess(alreadyGuessed):
#     # return letter entered by player. This checks for only a single letter
#     while True:
#         print('Guess a letter!')
#         guess = input()
#         guess = guess.lower()
#         if len(guess) != 1:
#             print('Please enter only a single letter.')
#         elif guess in alreadyGuessed:
#             print('You already guessed that letter! Choose another')
#         elif guess not in 'abcdefghijklmnopqrstuvwxyz':
#             print('Are you sure that you entered a letter?')
#         else:
#             return guess


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print(game_running)


@ client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$newgame'):
        print('$newgame received')
        game_running = True
        print(game_running)

        with open("words.txt", "r") as f:
            word_list = f.read().splitlines()

        word = random.choice(word_list)
        secretWord = word
        missedLetters = ''
        correctLetters = ''

        while game_running:
            await message.channel.send(HANGMAN_PICS[0])

            if message.content.startswith

        # while game_running:
        #     displayBoard(missedLetters, correctLetters, secretWord)

        #     guess = getGuess(missedLetters + correctLetters)

        #     if guess in secretWord:
        #         correctLetters = correctLetters + guess

        #         # check for win
        #         foundAllLetters = True
        #         for i in range(len(secretWord)):
        #             if secretWord[i] not in correctLetters:
        #                 foundAllLetters = False
        #                 break
        #         if foundAllLetters:
        #             print('Yes! The secret word is "' + secretWord + '"! You have won!')
        #             game_running = False
        #     else:
        #         missedLetters = missedLetters + guess

        #         # check if there are guesses left, if no then it's a loss
        #         if len(missedLetters) == len(HANGMAN_PICS) - 1:
        #             displayBoard(missedLetters, correctLetters, secretWord)
        #             print('You ran out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses. The word was "' + secretWord + '".')
        #             game_running = False

        # print(word)
        # print(len(word))
        # print('guesses available = ' + str(guesses))
        # await message.channel.send(f'Word has been selected. It is ' + str(len(word)) + ' characters long.')

    elif message.content.startswith('$endgame'):
        print('$endgame received')
        game_running = False
        print(game_running)
        await message.channel.send(f'Game has been ended.')

    else:
        await message.channel.send(f'some kinda fuckin error')


client.run('MTA5Mzk4OTMwMjQ5ODc3NTA3MA.GXXmu0.QpJoc_-B9cOkcte6w4quyDYQeaSZtTI_nF463A')
