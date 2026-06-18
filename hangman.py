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
        self.scores = []
        self.load_highscores()

    def load_highscores(self):
        try:
            with open('highscores.json') as f:
                self.scores = json.load(f)
        except FileNotFoundError:
            self.scores = []

    def save_highscores(self):
        with open('highscores.json', 'w') as f:
            json.dump(sorted(self.scores)[:5], f)

    def calculate_score(self, lives_remaining, word_length):
        return (lives_remaining * 10) + (word_length * 5)

    def play(self):
        # Game logic here
        pass

    def end_game(self, word, lives_remaining):
        score = self.calculate_score(lives_remaining, len(word))
        self.scores.append(score)
        self.save_highscores()
