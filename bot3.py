import discord
import random
import asyncio
import my_token

token_to_use = my_token.mytoken

word_list = []
game_running = False


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        
        print(game_running)

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('$guess'):
            await message.channel.send('Guess a number between 1 and 10.')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'Sorry, you took too long it was {answer}.')

            if int(guess.content) == answer:
                await message.channel.send('You are right!')
            else:
                await message.channel.send(f'Oops. It is actually {answer}.')

        if message.content.startswith('$newgame'):
            game_running = True
            with open("words.txt", "r") as f:
                word_list = f.read().splitlines()

            word = random.choice(word_list)
            print(word)

            await message.channel.send('Starting hangman game. Word is ' + str(len(word)) + ' characters long.')
            
            while game_running:
                
                guesses = 6

            # alreadyGuessed = []
            # toomuch = ('I told you only a single letter.')
            # alreadydone = ('You already guessed that letter! Choose another.')
            # realletter = ('Are you sure that you entered a letter?')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token_to_use)
