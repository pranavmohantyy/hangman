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
        self.hints_used = 0

    def choose_word(self):
        ...

    def reveal_hint(self, word):
        if self.hints_used < 1:
            for letter in word:
                if letter not in self.guessed_letters:
                    self.hints_used += 1
                    self.lives -= 1
                    return letter
        return None

    def play_game(self):
        ...
