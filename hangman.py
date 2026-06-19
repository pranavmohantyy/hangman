import random
import json
from colorama import Fore, Style

class Hangman:
    def __init__(self):
        with open('words.json') as f:
            self.word_bank = json.load(f)
        self.max_failures = 6
        self.stages = [
            f"{Fore.YELLOW}






{Style.RESET_ALL}",
            f"{Fore.YELLOW}______\n|    |\n|    O\n|   /|\n|   / \\n|{Style.RESET_ALL}",
            f"{Fore.YELLOW}______\n|    |\n|    O\n|   /|\n|   /\n|{Style.RESET_ALL}",
            f"{Fore.YELLOW}______\n|    |\n|    O\n|    |\n|   / \\n|{Style.RESET_ALL}",
            f"{Fore.YELLOW}______\n|    |\n|    O\n|    |\n|   /\n|{Style.RESET_ALL}",
            f"{Fore.YELLOW}______\n|    |\n|    O\n|    |\n|\n|{Style.RESET_ALL}",
            f"{Fore.YELLOW}______\n|    |\n|\n|\n|\n|{Style.RESET_ALL}",
        ]
        self.hints_used = 0

    def play(self):
        # game logic here
        pass
