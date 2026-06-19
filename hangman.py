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
            f"{Fore.YELLOW}______\n|    |\n|    O\n|   /|\n|    |\n|{Style.RESET_ALL}",
            f"{Fore.YELLOW}______\n|    |\n|    O\n|    |\n|   / \\n|{Style.RESET_ALL}",
            f"{Fore.YELLOW}______\n|    |\n|    O\n|    |\n|{Style.RESET_ALL}",
        ]

    def start_game(self):
        category = self.choose_category()
        word = random.choice(self.word_bank[category])
        guessed_letters = []
        failures = 0
        while failures < self.max_failures:
            print(self.display_hangman(failures))
            print(self.display_word(word, guessed_letters))
            guess = self.get_guess(guessed_letters)
            if guess in word:
                guessed_letters.append(guess)
                if all(letter in guessed_letters for letter in word):
                    print(f"You win! The word was '{word}'.")
                    return
            else:
                failures += 1
                guessed_letters.append(guess)
        print(self.display_hangman(failures))
        print(f"You lose! The word was '{word}'.")

    def choose_category(self):
        categories = list(self.word_bank.keys())
        print("Choose a category:")
        for i, category in enumerate(categories):
            print(f"{i + 1}. {category}")
        choice = int(input()) - 1
        return categories[choice]

    def display_hangman(self, failures):
        return self.stages[failures]

    def display_word(self, word, guessed_letters):
        return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

    def get_guess(self, guessed_letters):
        while True:
            guess = input("Guess a letter: ").lower()
            if guess.isalpha() and len(guess) == 1 and guess not in guessed_letters:
                return guess
            print("Invalid guess. Try again.")

if __name__ == '__main__':
    game = Hangman()
    game.start_game()