import random
import time

import pyttsx3
import simpleaudio as sa

from music.chord_progression import ChordProgression


class MusicGenerator:
    note_files = {
        'C': 'audio/C.wav',
        'C#': 'audio/CSharp.wav',
        'D': 'audio/D.wav',
        'D#': 'audio/DSharp.wav',
        'E': 'audio/E.wav',
        'F': 'audio/F.wav',
        'F#': 'audio/FSharp.wav',
        'G': 'audio/G.wav',
        'G#': 'audio/GSharp.wav',
        'A': 'audio/A.wav',
        'A#': 'audio/ASharp.wav',
        'B': 'audio/B.wav',
        'Bb': 'audio/BFlat.wav',
        'Db': 'audio/DFlat.wav',
        'Eb': 'audio/EFlat.wav',
        'Gb': 'audio/GFlat.wav',
    }

    chord_files = {
        'AMajor': 'audio/AMajor.m4a.wav',
        'AMinor': 'audio/AMinor.m4a.wav',
        'ASharpMajor': 'audio/ASharpMajor.m4a.wav',
        'ASharpMinor': 'audio/ASharpMinor.m4a.wav',
        'AFlatMajor': 'audio/AFlatMajor.m4a.wav',
        'AFlatMinor': 'audio/AFlatMinor.m4a.wav',
        'BMajor': 'audio/BMajor.m4a.wav',
        'BMinor': 'audio/BMinor.m4a.wav',
        'BFlatMajor': 'audio/BFlatMajor.m4a.wav',
        'BFlatMinor': 'audio/BFlatMinor.m4a.wav',
        'CMajor': 'audio/CMajor.m4a.wav',
        'CMinor': 'audio/CMinor.m4a.wav',
        'CSharpMajor': 'audio/CSharpMajor.m4a.wav',
        'CSharpMinor': 'audio/CSharpMinor.m4a.wav',
        'DMajor': 'audio/DMajor.m4a.wav',
        'DMinor': 'audio/DMinor.m4a.wav',
        'DSharpMajor': 'audio/DSharpMajor.m4a.wav',
        'DSharpMinor': 'audio/DSharpMinor.m4a.wav',
        'DFlatMajor': 'audio/DFlatMajor.m4a.wav',
        'DFlatMinor': 'audio/DFlatMinor.m4a.wav',
        'EMajor': 'audio/EMajor.m4a.wav',
        'EMinor': 'audio/EMinor.m4a.wav',
        'EFlatMajor': 'audio/EFlatMajor.m4a.wav',
        'EFlatMinor': 'audio/EFlatMinor.m4a.wav',
        'FMajor': 'audio/FMajor.m4a.wav',
        'FMinor': 'audio/FMinor.m4a.wav',
        'FSharpMajor': 'audio/FSharpMajor.m4a.wav',
        'FSharpMinor': 'audio/FSharpMinor.m4a.wav',
        'GMajor': 'audio/GMajor.m4a.wav',
        'GMinor': 'audio/GMinor.m4a.wav',
        'GSharpMajor': 'audio/GSharpMajor.m4a.wav',
        'GSharpMinor': 'audio/GSharpMinor.m4a.wav',
        'GFlatMajor': 'audio/GFlatMajor.m4a.wav',
        'GFlatMinor': 'audio/GFlatMinor.m4a.wav',
        
        'ADim': "audio/ADim.m4a.wav",
        'ASharpDim': "audio/ASharpDim.m4a.wav",
        'AFlatDim': "audio/AFlatDim.m4a.wav",
        'BDim': "audio/BDim.m4a.wav",
        'BFlatDim': "audio/BFlatDim.m4a.wav",
        'CDim': "audio/CDim.m4a.wav",
        'CSharpDim': "audio/CSharpDim.m4a.wav",
        'CFlatDim': "audio/CFlatDim.m4a.wav",
        'DDim': "audio/DDim.m4a.wav",
        'DSharpDim': "audio/DSharpDim.m4a.wav",
        'DFlatDim': "audio/DFlatDim.m4a.wav",
        'EDim': "audio/EDim.m4a.wav",
        'EFlatDim': "audio/EFlatDim.m4a.wav",
        'FDim': "audio/FDim.m4a.wav",
        'FSharpDim': "audio/FSharpDim.m4a.wav",
        'GDim': "audio/GDim.m4a.wav",
        'GSharpDim': "audio/GDim.m4a.wav",
        'GFlatDim': "audio/GFlatDim.m4a.wav",
    }

    def __init__(self, scale, bpm):
        self.scale = scale
        self.bpm = bpm
        self.engine = pyttsx3.init()

    def generate_random_note_from_scale(self):
        """Continuously generates a random note from the given scale every beat, where the tempo is defined by 'bpm' (beats per minute),
        and uses text-to-speech to speak the note name."""
        interval_seconds = 60 / self.bpm

        while True:
            note = random.choice(self.scale.build_scale())
            print(note)
            try:
                wave_obj = sa.WaveObject.from_wave_file(self.note_files[note])
                play_obj = wave_obj.play()
            except Exception as e:
                print(f"Failed to play the note: {e}")
            time.sleep(interval_seconds)

    def generate_random_chord_from_scale(self):
        """Continuously generates a random chord from the given scale every beat, where the tempo is defined by 'bpm' (beats per minute),
        and plays the corresponding audio file."""
        interval_seconds = 60 / self.bpm

        while True:
            chord = self.generate_random_chord()
            print(chord)
            try:
                wave_obj = sa.WaveObject.from_wave_file(self.chord_files[chord])
                play_obj = wave_obj.play()
                play_obj.wait_done()  # Wait for the audio to finish playing
            except Exception as e:
                raise ValueError(f"Failed to play the chord: {e}")
            time.sleep(interval_seconds)

    def generate_random_chord(self):
        """Generates a random chord from the given scale."""
        chord_progression = ChordProgression(self.scale)
        scale_degree = random.randint(1, 7)
        chord_progression.add_chord(scale_degree)
        _, chord = chord_progression.progression[-1]
        return chord

    @staticmethod
    def generate_random_notes(n):
        """Generate a random string of notes."""
        musical_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        return [random.choice(musical_alphabet) for _ in range(n)]

    @staticmethod
    def generate_random_chord_progression(scale, n):
        """Generate a random chord progression."""
        progression = ChordProgression(scale)
        for _ in range(n):
            scale_degree = random.randint(1, 7)
            progression.add_chord(scale_degree)
        return progression
