import unittest

from .scale import *


class TestScale(unittest.TestCase):

    def test_valid_initialization(self):
        scale = Scale('C')
        self.assertEqual(scale.root, 'C')
        self.assertFalse(scale.use_flats)
        self.assertEqual(scale.notes, Scale.SHARP_NOTES)

        scale = Scale('F', use_flats=True)
        self.assertEqual(scale.root, 'F')
        self.assertTrue(scale.use_flats)
        self.assertEqual(scale.notes, Scale.FLAT_NOTES)

    def test_invalid_initialization(self):
        with self.assertRaises(ValueError):
            Scale('H')
        with self.assertRaises(ValueError):
            Scale('C#b')

    def test_major_scale(self):
        # Sharp notes case
        scale = MajorScale('C')
        self.assertEqual(scale.build_scale(), ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        self.assertEqual(scale.get_intervals(), ['1', '2', '3', '4', '5', '6', '7'])

        # Flat notes case
        scale = MajorScale('F', use_flats=True)
        self.assertEqual(scale.build_scale(), ['F', 'G', 'A', 'Bb', 'C', 'D', 'E'])
        self.assertEqual(scale.get_intervals(), ['1', '2', '3', '4', '5', '6', '7'])

        # Sharp notes explicitly
        scale = MajorScale('F', use_flats=False)
        self.assertEqual(scale.build_scale(), ['F', 'G', 'A', 'A#', 'C', 'D', 'E'])
        self.assertEqual(scale.get_intervals(), ['1', '2', '3', '4', '5', '6', '7'])

    def test_natural_minor_scale(self):
        # Sharp notes case
        scale = NaturalMinorScale('A')
        self.assertEqual(scale.build_scale(), ['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        self.assertEqual(scale.get_intervals(), ['1', '2', '#2', '4', '5', '#5', '#6'])

        # Flat notes case
        scale = NaturalMinorScale('D', use_flats=True)
        self.assertEqual(scale.build_scale(), ['D', 'E', 'F', 'G', 'A', 'Bb', 'C'])
        self.assertEqual(scale.get_intervals(), ['1', '2', 'b3', '4', '5', 'b6', 'b7'])

        # Sharp notes explicitly
        scale = NaturalMinorScale('D', use_flats=False)
        self.assertEqual(scale.build_scale(), ['D', 'E', 'F', 'G', 'A', 'A#', 'C'])
        self.assertEqual(scale.get_intervals(), ['1', '2', '#2', '4', '5', '#5', '#6'])

    def test_harmonic_minor_scale(self):
        # Sharp notes case (use_flats=False)
        scale = HarmonicMinorScale('A')
        self.assertEqual(scale.build_scale(), ['A', 'B', 'C', 'D', 'E', 'F', 'G#'])
        self.assertEqual(scale.get_intervals(), ['1', '2', '#2', '4', '5', '#5', '7'])

        # Flat notes case (use_flats=True)
        scale = HarmonicMinorScale('D', use_flats=True)
        self.assertEqual(scale.build_scale(), ['D', 'E', 'F', 'G', 'A', 'Bb', 'Db'])
        self.assertEqual(scale.get_intervals(), ['1', '2', 'b3', '4', '5', 'b6', '7'])

        # Sharp notes explicitly (use_flats=False)
        scale = HarmonicMinorScale('D', use_flats=False)
        self.assertEqual(scale.build_scale(), ['D', 'E', 'F', 'G', 'A', 'A#', 'C#'])
        self.assertEqual(scale.get_intervals(), ['1', '2', '#2', '4', '5', '#5', '7'])

    def test_melodic_minor_scale(self):
        # Sharp notes case
        scale = MelodicMinorScale('A')
        self.assertEqual(scale.build_scale(), ['A', 'B', 'C', 'D', 'E', 'F#', 'G#'])
        self.assertEqual(scale.get_intervals(), ['1', '2', '#2', '4', '5', '6', '7'])

        # Flat notes case
        scale = MelodicMinorScale('D', use_flats=True)
        self.assertEqual(scale.build_scale(), ['D', 'E', 'F', 'G', 'A', 'B', 'Db'])
        self.assertEqual(scale.get_intervals(), ['1', '2', 'b3', '4', '5', '6', '7'])

        # Sharp notes explicitly
        scale = MelodicMinorScale('D', use_flats=False)
        self.assertEqual(scale.build_scale(), ['D', 'E', 'F', 'G', 'A', 'B', 'C#'])
        self.assertEqual(scale.get_intervals(), ['1', '2', '#2', '4', '5', '6', '7'])

    def test_pentatonic_scale_major(self):
        # Sharp notes case
        scale = PentatonicScale('C')
        self.assertEqual(scale.build_scale(), ['C', 'D', 'E', 'G', 'A'])
        self.assertEqual(scale.get_intervals(), ['1', '2', '3', '5', '6'])

        # Flat notes case
        scale = PentatonicScale('F', use_flats=True)
        self.assertEqual(scale.build_scale(), ['F', 'G', 'A', 'C', 'D'])
        self.assertEqual(scale.get_intervals(), ['1', '2', '3', '5', '6'])

        # Sharp notes explicitly
        scale = PentatonicScale('F', use_flats=False)
        self.assertEqual(scale.build_scale(), ['F', 'G', 'A', 'C', 'D'])
        self.assertEqual(scale.get_intervals(), ['1', '2', '3', '5', '6'])

    def test_pentatonic_scale_minor(self):
        # Sharp notes case
        scale = PentatonicScale('Am')
        self.assertEqual(scale.build_scale(), ['A', 'C', 'D', 'E', 'G'])
        self.assertEqual(scale.get_intervals(), ['1', '#2', '4', '5', '#6'])

        # Flat notes case
        scale = PentatonicScale('Dm', use_flats=True)
        self.assertEqual(scale.build_scale(), ['D', 'F', 'G', 'A', 'C'])
        self.assertEqual(scale.get_intervals(), ['1', 'b3', '4', '5', 'b7'])

        # Sharp notes explicitly
        scale = PentatonicScale('Dm', use_flats=False)
        self.assertEqual(scale.build_scale(), ['D', 'F', 'G', 'A', 'C'])
        self.assertEqual(scale.get_intervals(), ['1', '#2', '4', '5', '#6'])

    def test_modes(self):
        # Ionian
        ionian = IonianScale('C')
        self.assertEqual(ionian.build_scale(), ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        self.assertEqual(ionian.get_intervals(), ['1', '2', '3', '4', '5', '6', '7'])

        # Dorian
        dorian = DorianScale('D')
        self.assertEqual(dorian.build_scale(), ['D', 'E', 'F', 'G', 'A', 'B', 'C'])
        self.assertEqual(dorian.get_intervals(), ['1', '2', '#2', '4', '5', '6', '#6'])

        # Phrygian
        phrygian = PhrygianScale('E')
        self.assertEqual(phrygian.build_scale(), ['E', 'F', 'G', 'A', 'B', 'C', 'D'])
        self.assertEqual(phrygian.get_intervals(), ['1', '#1', '#2', '4', '5', '#5', '#6'])

        # Lydian
        lydian = LydianScale('F')
        self.assertEqual(lydian.build_scale(), ['F', 'G', 'A', 'B', 'C', 'D', 'E'])
        self.assertEqual(lydian.get_intervals(), ['1', '2', '3', '#4', '5', '6', '7'])

        # Mixolydian
        mixolydian = MixolydianScale('G')
        self.assertEqual(mixolydian.build_scale(), ['G', 'A', 'B', 'C', 'D', 'E', 'F'])
        self.assertEqual(mixolydian.get_intervals(), ['1', '2', '3', '4', '5', '6', '#6'])

        # Aeolian
        aeolian = AeolianScale('A')
        self.assertEqual(aeolian.build_scale(), ['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        self.assertEqual(aeolian.get_intervals(), ['1', '2', '#2', '4', '5', '#5', '#6'])

        # Locrian
        locrian = LocrianScale('B')
        self.assertEqual(locrian.build_scale(), ['B', 'C', 'D', 'E', 'F', 'G', 'A'])
        self.assertEqual(locrian.get_intervals(), ['1', '#1', '#2', '4', '#4', '#5', '#6'])

    def test_str_representation(self):
        scale = MajorScale('C')
        self.assertEqual(str(scale), 'MajorScale in C: C D E F G A B')

        scale = NaturalMinorScale('A')
        self.assertEqual(str(scale), 'NaturalMinorScale in A: A B C D E F G')


class TestScaleComparisons(unittest.TestCase):

    def setUp(self):
        self.major_c = MajorScale('C')
        self.natural_minor_a = NaturalMinorScale('A')
        self.major_g = MajorScale('G')
        self.dorian_d = DorianScale('D')
        self.phrygian_e = PhrygianScale('E', use_flats=True)

    def test_what_do_i_have_that_you_do_not(self):
        # Major C vs. Natural Minor A
        with self.subTest("Major C vs Natural Minor A"):
            # print(self.major_c)
            # print(self.natural_minor_a)
            self.assertEqual(self.major_c.what_do_i_have_that_you_do_not(self.natural_minor_a), set())

        # Major G vs. Dorian D
        with self.subTest("Major G vs Dorian D"):
            # print(self.major_g)
            # print(self.dorian_d)
            self.assertEqual(self.major_g.what_do_i_have_that_you_do_not(self.dorian_d), {'F#'})

        # Phrygian E (flats) vs. Major G
        with self.subTest("Phrygian E (flats) vs Major G"):
            print(self.major_g)
            print(self.phrygian_e)
            self.assertEqual(self.phrygian_e.what_do_i_have_that_you_do_not(self.major_g), {"F"})

    def test_what_do_you_have_i_do_not(self):
        # Major C vs. Natural Minor A
        with self.subTest("Major C vs Natural Minor A"):
            self.assertEqual(self.major_c.what_do_you_have_i_do_not(self.natural_minor_a), set())

        # Major G vs. Dorian D
        with self.subTest("Major G vs Dorian D"):
            self.assertEqual(self.major_g.what_do_you_have_i_do_not(self.dorian_d), {'F'})

        # Phrygian E (flats) vs. Major G
        with self.subTest("Phrygian E (flats) vs Major G"):
            self.assertEqual(self.phrygian_e.what_do_you_have_i_do_not(self.major_g), {'F#'})

    def test_union(self):
        # Major C and Natural Minor A
        with self.subTest("Union of Major C and Natural Minor A"):
            self.assertEqual(self.major_c.union(self.natural_minor_a), {'C', 'D', 'E', 'F', 'G', 'A', 'B'})

        # # Major G and Dorian D
        # with self.subTest("Union of Major G and Dorian D"):
        #     self.assertEqual(self.major_g.union(self.dorian_d), {'D', 'E', 'F', 'F#', 'G', 'A', 'B', 'C'})
        #
        # # Phrygian E (flats) and Major G
        # with self.subTest("Union of Phrygian E (flats) and Major G"):
        #     self.assertEqual(self.phrygian_e.union(self.major_g),
        #                      {'E', 'F#', 'G', 'A', 'B', 'C', 'D', 'Eb', 'Ab', 'Bb'})


class TestScaleConversion(unittest.TestCase):

    def test_convert_to_flats(self):
        # Sharp notes case
        scale = MajorScale('G', use_flats=False)
        scale = scale.to_flats()
        self.assertEqual(scale.build_scale(), ['G', 'A', 'B', 'C', 'D', 'E', 'Gb'])

        # Already flat notes case
        scale = MajorScale('F', use_flats=True)
        scale = scale.to_flats()
        self.assertEqual(scale.build_scale(), ['F', 'G', 'A', 'Bb', 'C', 'D', 'E'])

    def test_convert_to_sharps(self):
        # Flat notes case
        scale = MajorScale('Ab', use_flats=True)
        scale = scale.to_sharps()
        self.assertEqual(scale.build_scale(), ['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G'])


if __name__ == '__main__':
    unittest.main()
