import random
import json

class Hangman:
    def __init__(self):
        with open('words.json') as f:
            self.word_bank = json.load(f)
        self.max_failures = 6
        self.stages = [
            "\n\n\n\n\n\n\n",
            "______\n|    |\n|    O\n|   /|\n|   / \\n|\n",
            "______\n|    |\n|    O\n|   /|\n|   /\n|\n",
            "______\n|    |\n|    O\n|    |\n|   / \\n|\n",
            "______\n|    |\n|    O\n|    |\n|   /\n|\n",
            "______\n|    |\n|    O\n|    |\n|\n|\n",
            "______\n|    |\n|\n|\n|\n|\n"
        ]

    def choose_word(self):
        category = input('Choose a category (animals, countries, movies, technology): ')
        word = random.choice(self.word_bank[category])
        return word

    def display_word(self, word, guessed_letters):
        return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

    def play(self):
        word = self.choose_word()
        guessed_letters = set()
        failures = 0

        while failures < self.max_failures:
            print(self.stages[failures])
            print(self.display_word(word, guessed_letters))
            guess = input('Guess a letter: ').lower()
            if guess in guessed_letters:
                print('You already guessed that letter.')
                continue
            guessed_letters.add(guess)
            if guess not in word:
                failures += 1
            if all(letter in guessed_letters for letter in word):
                print(f'Congratulations! You guessed the word: {word}')
                return
        print(f'Sorry, you lost! The word was: {word}')

if __name__ == '__main__':
    game = Hangman()
    game.play()