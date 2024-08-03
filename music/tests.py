import unittest

from music.chord_progression import ChordProgression
from music.scale import Scale, PentatonicScale, MajorScale, MinorScale


class TestScale(unittest.TestCase):

    def test_valid_scale_initialization(self):
        scale = Scale('C')
        self.assertEqual(scale.root, 'C')
        self.assertEqual(scale.notes, Scale.SHARP_NOTES)

    def test_invalid_scale_initialization(self):
        with self.assertRaises(ValueError):
            Scale('H')

    def test_scale_with_flats(self):
        scale = Scale('Bb', use_flats=True)
        self.assertEqual(scale.root, 'Bb')
        self.assertEqual(scale.notes, Scale.FLAT_NOTES)

    def test_major_scale_build(self):
        scale = MajorScale('C')
        self.assertEqual(scale.build_scale(), ['C', 'D', 'E', 'F', 'G', 'A', 'B'])

    def test_minor_scale_build(self):
        scale = MinorScale('A')
        self.assertEqual(scale.build_scale(), ['A', 'B', 'C', 'D', 'E', 'F', 'G'])

    def test_pentatonic_major_scale_build(self):
        scale = PentatonicScale('C')
        self.assertEqual(scale.build_scale(), ['C', 'D', 'E', 'G', 'A'])

    def test_pentatonic_minor_scale_build(self):
        scale = PentatonicScale('Am')
        self.assertEqual(scale.build_scale(), ['A', 'C', 'D', 'E', 'G'])

    def test_what_do_i_have_that_you_do_not(self):
        scale1 = MajorScale('C')
        scale2 = MajorScale('G')
        self.assertEqual(scale1.what_do_i_have_that_you_do_not(scale2), {'F'})

    def test_what_do_you_have_i_do_not(self):
        scale1 = MajorScale('C')
        scale2 = MajorScale('G')
        self.assertEqual(scale1.what_do_you_have_i_do_not(scale2), {'F#'})

    def test_union(self):
        scale1 = MajorScale('C')
        scale2 = MajorScale('G')
        self.assertEqual(scale1.union(scale2), {'C', 'D', 'E', 'F', 'F#', 'G', 'A', 'B'})


class TestChordProgression(unittest.TestCase):

    def test_add_chord(self):
        scale = MajorScale('C')
        progression = ChordProgression(scale)
        progression.add_chord(1)
        self.assertEqual(progression.get_progression(), 'I (CMajor)')

    def test_invalid_chord(self):
        scale = MajorScale('C')
        progression = ChordProgression(scale)
        with self.assertRaises(ValueError):
            progression.add_chord(8)

    def test_chord_progression(self):
        scale = MajorScale('C')
        progression = ChordProgression(scale)
        progression.add_chord(1)
        progression.add_chord(4)
        progression.add_chord(5)
        self.assertEqual(progression.get_progression(), 'I (CMajor) - IV (FMajor) - V (GMajor)')


if __name__ == '__main__':
    unittest.main()
