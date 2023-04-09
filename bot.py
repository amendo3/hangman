import discord
import random

word_list = []
word = ""
display_word = ""
letters_guessed = []
guesses = 0

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('Logged in as (0.user)'.format(client))


@client.event
async def on_message(message):
    global word, display_word, letters_guessed, guesses

    if message.content == "!newgame":
        print('newgame received')
        with open("words.txt", "r") as f:
            word_list = f.read().splitlines()

        word = random.choice(word_list)
        guesses = 7
        letters_guessed = []
        display_word = "_" * len(word)
        await message.channel.send(f"New game! Guess the word: {display_word}")

    elif guesses > 0 and not message.author.bot:
        guess = message.content.lower()

        if len(guess) == 1 and guess.isalpha() and guess not in letters_guessed:
            letters_guessed.append(guess)

            if guess in word:
                for i in range(len(word)):
                    if word[i] == guess:
                        display_word = display_word[:i] + guess + display_word[i + 1:]
                await message.channel.send(f"{guess} is correct! {display_word}")

                if "_" not in display_word:
                    await message.channel.send("Congratulations! You won!")
                    guesses = 0

            else:
                guesses -= 1
                await message.channel.send(f"{guess} is incorrect! You have {guesses} guesses left.")

                if guesses == 0:
                    await message.channel.send(f"You lost! The word was {word}.")

print('Starting bot....')
client.run('MTA5Mzk4OTMwMjQ5ODc3NTA3MA.GXXmu0.QpJoc_-B9cOkcte6w4quyDYQeaSZtTI_nF463A')
