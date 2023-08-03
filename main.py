from midiutil.MidiFile import MIDIFile

def add_chord(track, time, duration, chord_notes):
    for note in chord_notes:
        track.addNote(0, 0, note, time, duration, 100)

# Chords for the song
verse1_chords = [['E', 'G', 'B', 'D'], ['E', 'G', 'B', 'D'], ['A', 'C', 'E', 'G'],
                 ['E', 'G', 'B', 'D'], ['A', 'C', 'E', 'G']]

chorus_chords = [['C', 'E', 'G', 'B'], ['C', 'E', 'G', 'B'], ['C', 'E', 'G', 'B'],
                 ['A', 'C', 'E', 'G']]

verse2_chords = [['E', 'G', 'B', 'D'], ['A', 'C', 'E', 'G'],
                 ['E', 'G', 'B', 'D'], ['A', 'C', 'E', 'G']]

bridge_chords = [['A', 'C', 'E', 'G'], ['C', 'E', 'G', 'B'],
                 ['A', 'C', 'E', 'G'], ['C', 'E', 'G', 'B']]

outro_chords = [['E', 'G', 'B', 'D'], ['E', 'G', 'B', 'D'],
                ['E', 'G', 'B', 'D'], ['E', 'G', 'B', 'D']]

# Create MIDI file and tracks
midi = MIDIFile(1)
track = 0
time = 0
duration = 1  # Duration in beats for each chord

# Add chords to the tracks
for chord in verse1_chords:
    add_chord(midi, track, time, duration, chord)
    time += duration

for chord in chorus_chords:
    add_chord(midi, track, time, duration, chord)
    time += duration

for chord in verse2_chords:
    add_chord(midi, track, time, duration, chord)
    time += duration

for chord in bridge_chords:
    add_chord(midi, track, time, duration, chord)
    time += duration

for chord in chorus_chords:
    add_chord(midi, track, time, duration, chord)
    time += duration

for chord in outro_chords:
    add_chord(midi, track, time, duration, chord)
    time += duration

# Save the MIDI file
with open("generated_song.mid", "wb") as output_file:
    midi.writeFile(output_file)
