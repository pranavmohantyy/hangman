import random
import json

class Hangman:
    def __init__(self):
        with open('words.json') as f:
            self.word_bank = json.load(f)
        self.max_failures = 6
        self.stages = [
            "\n\n\n\n\n\n\n",
            "______\n|    |\n|    O\n|   /|\n|   / \
|\n",
            "______\n|    |\n|    O\n|   /|\n|   /\n|\n",
            "______\n|    |\n|    O\n|    |\n|   / \
|\n",
            "______\n|    |\n|    O\n|    |\n|   /\n|\n",
            "______\n|    |\n|    O\n|    |\n|\n|\n",
            "______\n|    |\n|\n|\n|\n|\n"
        ]
        self.hints_used = 0
        self.difficulty = 'medium'
        self.set_difficulty()

    def set_difficulty(self):
        if self.difficulty == 'easy':
            self.max_failures = 8
        elif self.difficulty == 'hard':
            self.max_failures = 4
        else:
            self.max_failures = 6

    def choose_category(self, category):
        self.word = random.choice(self.word_bank[category])
        self.guesses = []
        self.failures = 0
        self.hints_used = 0

    def get_display_word(self):
        return ' '.join([letter if letter in self.guesses else '_' for letter in self.word])

    def make_guess(self, letter):
        if letter in self.guesses:
            return False
        self.guesses.append(letter)
        if letter not in self.word:
            self.failures += 1
        return True

    def get_stage(self):
        return self.stages[self.failures]

    def get_hint(self):
        if self.hints_used < 1:
            self.hints_used += 1
            return random.choice([letter for letter in self.word if letter not in self.guesses])
        return None
