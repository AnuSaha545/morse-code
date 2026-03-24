import time
import platform
from config import DOT_DURATION, DASH_DURATION

try:
    import winsound
    SOUND_AVAILABLE = True
except ImportError:
    SOUND_AVAILABLE = False


def play_morse(code: str) -> None:
    """Play Morse code as audio or console visualization."""
    system = platform.system()

    for char in code:
        if char == ".":
            duration = DOT_DURATION
        elif char == "-":
            duration = DASH_DURATION
        else:
            time.sleep(DOT_DURATION)
            continue

        if system == "Windows" and SOUND_AVAILABLE:
            winsound.Beep(800, int(duration * 1000))
        else:
            print(char, end="", flush=True)

        time.sleep(DOT_DURATION)