import random

class Hangman:
    def __init__(self):
        self.word_list = ['python', 'hangman', 'programming', 'developer', 'github']
        self.max_failures = 6
        self.stages = [
            "\n\n\n\n\n\n\n",
            "______\n|    |\n|    O\n|   /|\n|   / \\n|\n",
            "______\n|    |\n|    O\n|   /|\n|   /\n|\n",
            "______\n|    |\n|    O\n|    |\n|   / \\n|\n",
            "______\n|    |\n|    O\n|    |\n|   /\n|\n",
            "______\n|    |\n|    O\n|\n|\n|\n",
            "______\n|    |\n|\n|\n|\n|\n"
        ]

    def choose_word(self):
        return random.choice(self.word_list)

    def play(self):
        word = self.choose_word()
        guessed = ['_'] * len(word)
        failures = 0
        guessed_letters = []

        while failures < self.max_failures and '_' in guessed:
            print(self.stages[failures])
            print(' '.join(guessed))
            guess = input('Guess a letter: ').lower()

            if guess in guessed_letters:
                print('You already guessed that letter.')
                continue
            if guess in word:
                for index, letter in enumerate(word):
                    if letter == guess:
                        guessed[index] = guess
            else:
                failures += 1
            guessed_letters.append(guess)

        if '_' not in guessed:
            print('Congratulations! You guessed the word:', word)
        else:
            print(self.stages[failures])
            print('Game over! The word was:', word)

if __name__ == '__main__':
    game = Hangman()
    game.play()