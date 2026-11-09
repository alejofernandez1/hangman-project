"""Estado y reglas del juego Hangman."""


class HangmanGame:
    def __init__(self, word, max_errors=6):
        self.word = word.lower()
        self.guessed_letters = []
        self.max_errors = max_errors
        self.errors = 0

    def process_guess(self, letter):
        letter = letter.lower()
        if len(letter) != 1 or not letter.isalpha() or letter in self.guessed_letters:
            return False
        self.guessed_letters.append(letter)
        if letter not in self.word:
            self.errors += 1
            return False
        return True

    def display_progress(self):
        """Revela letras adivinadas y caracteres no alfabéticos."""
        return " ".join(
            char if not char.isalpha() or char.lower() in self.guessed_letters else "_"
            for char in self.word
        )

    def is_won(self):
        return all(not char.isalpha() or char.lower() in self.guessed_letters for char in self.word)

    def is_lost(self):
        return self.errors >= self.max_errors

    def draw_hangman(self):
        stages = [
            "  +---+\n  |   |\n      |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n  |   |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|   |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n=========",
        ]
        return stages[min(self.errors, self.max_errors)]
