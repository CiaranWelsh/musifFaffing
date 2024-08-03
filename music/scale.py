class Scale:
    SHARP_KEYS = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#']
    FLAT_KEYS = ['F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb']
    SHARP_NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    FLAT_NOTES = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

    def __init__(self, root, use_flats=False):
        if root not in self.SHARP_NOTES and root not in self.FLAT_NOTES:
            raise ValueError(f"Invalid root note: {root}")
        self.root = root
        self.use_flats = use_flats
        self.notes = self.FLAT_NOTES if use_flats else self.SHARP_NOTES

    def build_scale(self):
        """Builds the scale based on scale degrees."""
        root_index = self.notes.index(self.root)
        return [self.notes[(root_index + semitone) % len(self.notes)] for semitone in self.scale_degrees]

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

    def union(self, other_scale):
        """Returns the union of this scale and another."""
        my_notes = set(self.build_scale())
        other_notes = set(other_scale.build_scale())
        return my_notes.union(other_notes)


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


class MinorScale(Scale):
    def __init__(self, root, use_flats=False):
        super().__init__(root, use_flats)
        # Natural minor scale: root, major second, minor third, perfect fourth, perfect fifth, minor sixth, minor seventh
        self.scale_degrees = [0, 2, 3, 5, 7, 8, 10]
