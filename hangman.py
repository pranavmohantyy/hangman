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

    def choose_word(self, category):
        return random.choice(self.word_bank[category])

    # Other methods will go here...