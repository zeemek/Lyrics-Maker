# 🎶 LyricSync Romanticizer

**Author:** Laiadaba Meitei  
**Description:** Displays song title instantly and lyrics in perfect sync using timestamps.

---

## How to Use

1. Make sure you have Python installed (Python 3.x recommended).  
2. Save the script as `lyricsync.py`.  
3. Run the script using:

```bash
python lyricsync.py
```

The song title and artist will display immediately, and lyrics will appear line by line in sync with the timestamps.

---

## How to Customize

### Change Song Title and Artist
Edit the variables at the top of the script:

```python
song_title = "💖 Korouna Ningthina 💖"
artist = "By Laidaba"
```

### Change Lyrics
Modify the `lyrics` list with your own lines:

```python
lyrics = [
    "Line 1 of your song",
    "Line 2 of your song",
    "Line 3 of your song",
    ...
]
```

### Change Timestamps
Update the `timestamps` list to match your lyrics timing (in seconds):

```python
timestamps = [
    (0, 4),      # Line 1
    (4, 7),      # Line 2
    (8, 12),     # Line 3
    ...
]
```

**Important:** Each tuple corresponds to `(start_time, end_time)` for the respective lyric line. Make sure the number of timestamps matches the number of lyrics.

---

## Example

Here is a full example showing song title, artist, lyrics, and timestamps:

```python
# Song title and artist
song_title = "🌸 My Love Song 🌸"
artist = "By Example Artist"

# Lyrics
lyrics = [
    "I see you walking by 🌞",
    "Smiles that light the sky 🌈",
    "Heartbeats racing fast 💓"
]

# Timestamps in seconds
timestamps = [
    (0, 3),   # Line 1
    (3, 6),   # Line 2
    (6, 10)   # Line 3
]
```

When you run the script, the lyrics will appear with a typing animation, perfectly synced to the timestamps.

---

## Features
- Typing animation for each line.
- Perfectly synced with your defined timestamps.
- Easy to modify for any song.

