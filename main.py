"""Punto de entrada para jugar Hangman desde la terminal."""

from game import HangmanGame
from utils import get_random_word, read_letter

DIFFICULTIES = {
    "1": ("Fácil", 8),
    "2": ("Normal", 6),
    "3": ("Difícil", 4),
}


def choose_difficulty():
    print("\nDificultad: 1) Fácil  2) Normal  3) Difícil")
    while True:
        choice = input("Elige 1, 2 o 3: ").strip()
        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]
        print("Opción inválida.")


def play_round():
    difficulty, max_errors = choose_difficulty()
    game = HangmanGame(get_random_word(), max_errors=max_errors)
    print(f"\n¡Comienza Hangman! Dificultad: {difficulty}")

    while not game.is_won() and not game.is_lost():
        print("\n" + game.draw_hangman())
        print(f"Palabra: {game.display_progress()}")
        print("Letras intentadas: " + (", ".join(game.guessed_letters) or "ninguna"))
        print(f"Intentos incorrectos restantes: {game.max_errors - game.errors}")
        letter = read_letter(guessed_letters=game.guessed_letters)
        if game.process_guess(letter):
            print("¡Bien! La letra está en la palabra.")
        else:
            print("Esa letra no está en la palabra.")

    print("\n" + game.draw_hangman())
    if game.is_won():
        print(f"¡Ganaste! La palabra era: {game.word}")
    else:
        print(f"Fin del juego. La palabra era: {game.word}")


def main():
    print("=== AHORCADO / HANGMAN ===")
    while True:
        try:
            play_round()
        except RuntimeError as error:
            print(f"Error: {error}")
            return
        if input("\n¿Quieres jugar otra vez? (s/n): ").strip().lower() not in ("s", "si", "sí"):
            print("¡Gracias por jugar!")
            break


if __name__ == "__main__":
    main()
