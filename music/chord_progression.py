from music.scale import MajorScale, MinorScale


class ChordProgression:
    roman_numerals = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    note_mapping = {
        'C#': 'CSharp', 'Db': 'DFlat',
        'D#': 'DSharp', 'Eb': 'EFlat',
        'F#': 'FSharp', 'Gb': 'GFlat',
        'G#': 'GSharp', 'Ab': 'AFlat',
        'A#': 'ASharp', 'Bb': 'BFlat'
    }

    def __init__(self, scale):
        self.scale = scale.build_scale()
        self.progression = []

        # Adjust chord qualities based on the scale type
        if isinstance(scale, MajorScale):
            self.chord_qualities = ['M', 'm', 'm', 'M', 'M', 'm', 'd']
        elif isinstance(scale, MinorScale):
            self.chord_qualities = ['m', 'd', 'M', 'm', 'm', 'M', 'M']

    def add_chord(self, scale_degree):
        if 1 <= scale_degree <= len(self.scale):
            chord_root = self.scale[scale_degree - 1]
            chord_quality = self.chord_qualities[scale_degree - 1]

            # Standardize chord root name
            chord_root = self.note_mapping.get(chord_root, chord_root)

            roman_numeral = self.roman_numerals[scale_degree - 1]
            if chord_quality == 'm':
                roman_numeral = roman_numeral.lower()
                chord = chord_root + 'Minor'
            elif chord_quality == 'd':
                chord = chord_root + 'Dim'
            else:
                chord = chord_root + 'Major'

            self.progression.append((roman_numeral, chord))
        else:
            raise ValueError(f"Scale degree out of range: {scale_degree}")

    def get_progression(self):
        return ' - '.join([f"{func} ({chord})" for func, chord in self.progression])

    def __str__(self):
        return "Chord Progression: " + self.get_progression()
