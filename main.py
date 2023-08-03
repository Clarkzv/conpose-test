from pydub import AudioSegment
import time
import subprocess

# Define your chords and their durations (in seconds)
chords = [
    ("Em", 1),
    ("Cmaj7", 1),
    ("G", 1),
    ("D/F#", 1),
    ("Em", 1),
    ("Cmaj7", 1),
    ("G", 1),
    ("D", 1),
    ("Am", 1),
    ("G", 1),
    ("D", 1),
    ("Em", 1),
    ("Cmaj7", 1),
    ("G", 1),
    ("D/F#", 1),
    ("Am", 1),
    ("G", 1),
    ("D", 1),
    ("Em", 1),
    ("Cmaj7", 1),
    ("G", 1),
    ("D/F#", 1),
    ("Am", 1),
    ("G", 1),
    ("D", 1),
    ("Em", 1),
    ("Cmaj7", 1),
    ("G", 1),
    ("D", 1),
    ("Em", 1),
    ("Cmaj7", 1),
    ("G", 1),
    ("D/F#", 1),
    ("Em", 1),
    ("Cmaj7", 1),
    ("G", 1),
    ("D/F#", 1),
    ("Em", 1),
    ("Cmaj7", 1),
    ("G", 1),
    ("D", 1),
    ("Am", 1),
    ("G", 1),
    ("D", 1),
    ("Em", 1),
]

# Define the piano notes for each chord
piano_notes = {
    "Cmaj7": ["C4", "E4", "G4", "B4"],
    "Em": ["E3", "G3", "B3", "E4"],
    "G": ["G3", "B3", "D4", "G4"],
    "D/F#": ["D3", "F#3", "A3", "D4"],
}

# Function to convert note name to MIDI note number
def note_to_number(note):
    notes_dict = {"C": 0, "C#": 1, "Db": 1, "D": 2, "D#": 3, "Eb": 3, "E": 4,
                  "F": 5, "F#": 6, "Gb": 6, "G": 7, "G#": 8, "Ab": 8, "A": 9,
                  "A#": 10, "Bb": 10, "B": 11}
    note_name, octave = note[:-1], int(note[-1])
    return (octave + 1) * 12 + notes_dict[note_name]

# Function to create a chord AudioSegment
def create_chord(chord_name, duration):
    notes = piano_notes.get(chord_name)
    if not notes:
        raise ValueError(f"Invalid chord name: {chord_name}")
    
    chord_audio = AudioSegment.empty()
    for note in notes:
        midi_note = note_to_number(note)
        note_audio = AudioSegment.from_file(f"piano_samples/{midi_note}.wav")
        chord_audio += note_audio

    silence = AudioSegment.silent(duration=int(duration * 1000))
    return chord_audio + silence

# Create the entire song as an AudioSegment
song = AudioSegment.empty()
for chord, duration in chords:
    chord_audio = create_chord(chord, duration)
    song += chord_audio

# Export the song as a WAV file
wav_filename = "your_song.wav"
song.export(wav_filename, format="wav")

print(f"WAV file '{wav_filename}' created. You can listen to or further edit the song.")
