from typing import Dict

MORSE_CODE: Dict[str, str] = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
    " ": "/"
}

REVERSE_MORSE: Dict[str, str] = {v: k for k, v in MORSE_CODE.items()}

def text_to_morse(text: str) -> str:
    """Convert plain text to Morse code."""
    return " ".join(MORSE_CODE.get(char, "?") for char in text.upper())

def morse_to_text(code: str) -> str:
    """Convert Morse code to plain text."""
    if not code.strip():
        raise ValueError("Input Morse code is empty.")

    words = code.strip().split(" / ")
    decoded_words = []

    for word in words:
        letters = word.split()
        decoded_letters = [
            REVERSE_MORSE.get(symbol, "?") for symbol in letters
        ]
        decoded_words.append("".join(decoded_letters))

    return " ".join(decoded_words).title()