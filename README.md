# Hangman / Ahorcado

Juego de ahorcado para la terminal, escrito en Python 3.

## ¿Qué hace?

El programa elige una palabra al azar y pide al jugador que adivine sus letras. En cada turno muestra el progreso de la palabra, las letras intentadas y los errores restantes. El jugador gana al descubrir todas las letras antes de quedarse sin intentos. Se pueden elegir tres niveles de dificultad y empezar otra partida al terminar.

## Archivos

- `main.py`: inicia el juego, solicita la dificultad y administra los turnos.
- `game.py`: contiene la clase `HangmanGame`, que guarda el estado y comprueba las adivinanzas y el resultado.
- `utils.py`: elige una palabra al azar de la lista y valida las letras ingresadas.
- `wordlist.txt`: contiene las palabras posibles, una por línea.
