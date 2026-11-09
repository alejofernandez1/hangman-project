"""Funciones auxiliares para Hangman."""

from pathlib import Path
import random

BASE_DIR = Path(__file__).resolve().parent
WORDLIST_PATH = BASE_DIR / "wordlist.txt"


def get_random_word():
    """Lee palabras alfabéticas del archivo y devuelve una al azar."""
    try:
        words = [line.strip().lower() for line in WORDLIST_PATH.read_text(encoding="utf-8").splitlines()]
    except OSError as exc:
        raise RuntimeError(f"No se pudo leer {WORDLIST_PATH.name}: {exc}") from exc
    words = [word for word in words if word and word.isalpha()]
    if not words:
        raise RuntimeError("wordlist.txt no contiene palabras alfabéticas.")
    return random.choice(words)


def read_letter(prompt="Ingresa una letra: ", guessed_letters=None):
    """Solicita una letra alfabética que todavía no se haya intentado."""
    guessed_letters = guessed_letters or []
    while True:
        value = input(prompt).strip().lower()
        if len(value) != 1 or not value.isalpha():
            print("Entrada inválida: escribe exactamente una letra.")
        elif value in guessed_letters:
            print("Ya intentaste esa letra. Prueba con otra.")
        else:
            return value
