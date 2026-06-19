import random
import json
from collections import Counter
from colorama import Fore, Style

class Hangman:
    def __init__(self):
        with open('words.json') as f:
            self.word_bank = json.load(f)
        self.max_failures = 6
        self.stages = [
            f"{Fore.YELLOW}\n\n\n\n\n\n{Style.RESET_ALL}",
            f"{Fore.YELLOW}______\n|    |\n|    O\n|   /|\n|   / \\n|{Style.RESET_ALL}",
            f"{Fore.YELLOW}______\n|    |\n|    O\n|   /|\n|   /\n|{Style.RESET_ALL}",
            f"{Fore.YELLOW}______\n|    |\n|    O\n|    |\n|   / \\n|{Style.RESET_ALL}",
            f"{Fore.YELLOW}______\n|    |\n|    O\n|    |\n|    /\n|{Style.RESET_ALL}",
            f"{Fore.YELLOW}______\n|    |\n|    O\n|    |\n|   / \n|{Style.RESET_ALL}",
            f"{Fore.YELLOW}______\n|    |\n|    O\n|    |\n|   / \n|{Style.RESET_ALL}"
        ]
        self.score = 0

    def choose_word(self, category):
        return random.choice(self.word_bank[category])

    def get_letter_frequency(self, word, guessed_letters):
        remaining_letters = [letter for letter in word if letter not in guessed_letters]
        if not remaining_letters:
            return None
        letter_count = Counter(remaining_letters)
        return letter_count.most_common(1)[0][0]

    def play(self):
        category = input("Choose a category (animals, countries, movies, technology): ")
        word = self.choose_word(category)
        guessed_letters = []
        failures = 0

        while failures < self.max_failures:
            print(self.stages[failures])
            print('Current word:', ' '.join([letter if letter in guessed_letters else '_' for letter in word]))
            print('Guessed letters:', ' '.join(guessed_letters))

            if input('Do you want a hint for the most frequent letter? (y/n): ').lower() == 'y':
                hint = self.get_letter_frequency(word, guessed_letters)
                if hint:
                    print(f'The most common remaining letter is: {hint}')
                else:
                    print('No remaining letters to hint.')

            guess = input('Guess a letter: ').lower()
            if guess in guessed_letters:
                print('You already guessed that letter.')
                continue
            guessed_letters.append(guess)

            if guess not in word:
                failures += 1

        if failures == self.max_failures:
            print('You lost! The word was:', word)
        else:
            print('Congratulations! You guessed the word:', word)
            self.score += 1

if __name__ == '__main__':
    game = Hangman()
    game.play()