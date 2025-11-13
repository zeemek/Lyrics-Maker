# 🎶 LyricSync Romanticizer - Full Timestamp Synced Version
# Author: Laiadaba Meitei
# Description: Displays song title instantly and lyrics in perfect sync using timestamps.

import time
import sys

def type_effect(text, speed=0.04):
    """Displays text character by character for a typing animation."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()  # move to next line

if __name__ == "__main__":
    # 🎵 Song title
    song_title = "💖 Korouna Ningthina 💖"
    artist = "By Laidaba"
    print(f"{song_title}\n{artist}\n")

    # 💞 Lyrics
    lyrics = [
        "Korouna ningthina ngallaga🌞🌅",
        "Nanakta laklani eina 🚶‍♂️🚶‍♂️🚶‍♂️",
        "Ngairamkho nangbune ⏰",
        "Laijagi epomga loinana 🌊🌊🌊",
        "Tanik tanik pukningbu💝💝💝",
        "Themlage nahak ki👩👩👩",
    ]

    # ⏱ Timestamps for each line (start_time, end_time in seconds)
    timestamps = [
        (0, 4),      # Line 1
        (4, 7),      # Line 2
        (8, 12.5),   # Line 3
        (16, 19),    # Line 4
        (20, 24),  # Line 5
        (23.5, 30)   # Line 6
    ]

    start_time = time.time()

    # Display lyrics in timestamp sync
    for (line, (start, end)) in zip(lyrics, timestamps):
        # Wait until the exact start time
        while time.time() - start_time < start:
            time.sleep(0.01)

        # Calculate typing speed so line finishes exactly at end_time
        duration = end - start
        char_delay = duration / max(len(line), 1)

        type_effect(line, speed=char_delay)
