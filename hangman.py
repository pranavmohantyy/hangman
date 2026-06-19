import random
import json
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
            f"{Fore.YELLOW}______\n|    |\n|    O\n|    |\n|    / \\n|{Style.RESET_ALL}",
            f"{Fore.YELLOW}______\n|    |\n|    O\n|   /|\n|    / \\n|{Style.RESET_ALL}",
            f"{Fore.YELLOW}______\n|    |\n|    O\n|   /|\n|   / \\n|{Style.RESET_ALL}"
        ]
        self.wins = 0
        self.losses = 0
        self.current_word = ''
        self.hints = ''

    def choose_word(self):
        category = input('Choose a category (animals, countries, movies, technology): ')
        self.current_word = random.choice(self.word_bank.get(category, []))
        self.hints = self.get_hint()

    def get_hint(self):
        return f'The word is in the category: {category}'

    def play(self):
        self.choose_word()
        failures = 0
        guessed = []
        while failures < self.max_failures:
            print(self.stages[failures])
            print(self.get_current_state(guessed))
            guess = input('Guess a letter: ').lower()
            if guess in guessed:
                print('You already guessed that letter.')
                continue
            guessed.append(guess)
            if guess not in self.current_word:
                failures += 1
            if all(letter in guessed for letter in self.current_word):
                print('You win!')
                self.wins += 1
                break
        else:
            print('You lose!')
            self.losses += 1
        self.play_again()

    def get_current_state(self, guessed):
        return ''.join([letter if letter in guessed else '_' for letter in self.current_word])

    def play_again(self):
        print(f'Session stats - Wins: {self.wins}, Losses: {self.losses}')
        again = input('Play again? (y/n): ').lower()
        if again == 'y':
            self.play()

if __name__ == '__main__':
    game = Hangman()
    game.play()