from __future__ import annotations


class Scale:
    # notes
    SHARP_NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    FLAT_NOTES = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

    # intervals
    INTERVALS_SHARP = {0: '1', 1: '#1', 2: '2', 3: '#2', 4: '3', 5: '4', 6: '#4', 7: '5', 8: '#5', 9: '6', 10: '#6',
                       11: '7'}
    INTERVALS_FLAT = {0: '1', 1: 'b2', 2: '2', 3: 'b3', 4: '3', 5: '4', 6: 'b5', 7: '5', 8: 'b6', 9: '6', 10: 'b7',
                      11: '7'}

    def __init__(self, root, use_flats=False):
        if root not in self.SHARP_NOTES and root not in self.FLAT_NOTES:
            raise ValueError(f"Invalid root note: {root}")
        self.root = root
        self.use_flats = use_flats
        self.scale_degrees = []
        self.notes = self.FLAT_NOTES if use_flats else self.SHARP_NOTES
        self.intervals = self.INTERVALS_FLAT if self.use_flats else self.INTERVALS_SHARP

    def build_scale(self):
        """Builds the scale based on scale degrees."""
        root_index = self.notes.index(self.root)
        return [self.notes[(root_index + semitone) % len(self.notes)] for semitone in self.scale_degrees]

    def get_intervals(self):
        """Returns the intervals of the scale."""
        return [self.intervals[degree] for degree in self.scale_degrees]

    def __str__(self):
        return f"{self.__class__.__name__} in {self.root}: " + ' '.join(self.build_scale())

    def what_do_i_have_that_you_do_not(self, other_scale):
        """Returns the set difference between this scale and another."""
        my_notes = set(self.build_scale())
        other_notes = set(other_scale.build_scale())
        return my_notes.difference(other_notes)

    def what_do_you_have_i_do_not(self, other_scale):
        """Returns the set difference between this scale and another."""
        my_notes = set(self.build_scale())
        other_notes = set(other_scale.build_scale())
        return other_notes.difference(my_notes)

    def union(self, other_scale:Scale):
        """Returns the union of this scale and another."""
        my_notes = set(self.build_scale())
        # normalize the scale accidental convension
        other_scale = other_scale.to_flats() if self.use_flats else other_scale.to_sharps()
        other_notes = set(other_scale.build_scale())

        return my_notes.union(other_notes)

    def to_flats(self) -> Scale:
        """Converts the scale's notes from sharps to flats."""
        flat_root = self.root
        if not self.use_flats:
            flat_root = self.FLAT_NOTES[self.SHARP_NOTES.index(self.root)]
        return self.__class__(flat_root, use_flats=True)

    def to_sharps(self) -> Scale:
        """Converts the scale's notes from sharps to flats."""
        sharp_root = self.root
        if self.use_flats:
            sharp_root = self.SHARP_NOTES[self.FLAT_NOTES.index(self.root)]
        return self.__class__(sharp_root, use_flats=False)


class PentatonicScale(Scale):
    def __init__(self, scale_string, use_flats=False):
        root, scale_type = self.parse_scale_string(scale_string)
        super().__init__(root, use_flats)
        if scale_type == 'm':
            # Pentatonic minor: root, minor third, fourth, fifth, minor seventh
            self.scale_degrees = [0, 3, 5, 7, 10]
        else:
            # Pentatonic major: root, major second, major third, fifth, major sixth
            self.scale_degrees = [0, 2, 4, 7, 9]

    @staticmethod
    def parse_scale_string(scale_string):
        """Parses the scale string to extract the root note and scale type."""
        if scale_string.endswith('m'):
            return scale_string[:-1], 'm'
        else:
            return scale_string, 'M'


class MajorScale(Scale):
    def __init__(self, root, use_flats=False):
        super().__init__(root, use_flats)
        # Major scale: root, major second, major third, perfect fourth, perfect fifth, major sixth, major seventh
        self.scale_degrees = [0, 2, 4, 5, 7, 9, 11]


class NaturalMinorScale(Scale):
    def __init__(self, root, use_flats=False):
        super().__init__(root, use_flats)
        # Natural minor scale: root, major second, minor third, perfect fourth, perfect fifth, minor sixth, minor seventh
        self.scale_degrees = [0, 2, 3, 5, 7, 8, 10]


class HarmonicMinorScale(Scale):
    def __init__(self, root, use_flats=False):
        super().__init__(root, use_flats)
        # Harmonic minor scale: root, major second, minor third, perfect fourth, perfect fifth, minor sixth, major seventh
        self.scale_degrees = [0, 2, 3, 5, 7, 8, 11]


class MelodicMinorScale(Scale):
    def __init__(self, root, use_flats=False):
        super().__init__(root, use_flats)
        # Melodic minor scale: root, major second, minor third, perfect fourth, perfect fifth, major sixth, major seventh
        self.scale_degrees = [0, 2, 3, 5, 7, 9, 11]


class IonianScale(Scale):
    def __init__(self, root, use_flats=False):
        super().__init__(root, use_flats)
        # Ionian mode (same as Major scale)
        self.scale_degrees = [0, 2, 4, 5, 7, 9, 11]


class DorianScale(Scale):
    def __init__(self, root, use_flats=False):
        super().__init__(root, use_flats)
        # Dorian mode
        self.scale_degrees = [0, 2, 3, 5, 7, 9, 10]


class PhrygianScale(Scale):
    def __init__(self, root, use_flats=False):
        super().__init__(root, use_flats)
        # Phrygian mode
        self.scale_degrees = [0, 1, 3, 5, 7, 8, 10]


class LydianScale(Scale):
    def __init__(self, root, use_flats=False):
        super().__init__(root, use_flats)
        # Lydian mode
        self.scale_degrees = [0, 2, 4, 6, 7, 9, 11]


class MixolydianScale(Scale):
    def __init__(self, root, use_flats=False):
        super().__init__(root, use_flats)
        # Mixolydian mode
        self.scale_degrees = [0, 2, 4, 5, 7, 9, 10]


class AeolianScale(Scale):
    def __init__(self, root, use_flats=False):
        super().__init__(root, use_flats)
        # Aeolian mode (same as Natural Minor scale)
        self.scale_degrees = [0, 2, 3, 5, 7, 8, 10]


class LocrianScale(Scale):
    def __init__(self, root, use_flats=False):
        super().__init__(root, use_flats)
        # Locrian mode
        self.scale_degrees = [0, 1, 3, 5, 6, 8, 10]
