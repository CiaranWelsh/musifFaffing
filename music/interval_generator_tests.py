

import unittest
from unittest.mock import patch, call, MagicMock

from music.interval_generator import IntervalAudioGenerator
from music.scale import MajorScale, MinorScale

class TestIntervalAudioGenerator(unittest.TestCase):
    @patch('simpleaudio.WaveObject.from_wave_file')
    @patch('simpleaudio.PlayObject')
    def test_major_scale_sharps(self, mock_wave_object, mock_play_object):
        scale = MajorScale('G', use_flats=False)  # G major uses sharps
        generator = IntervalAudioGenerator(scale, bpm=60, use_extended=False, octave_preference='both')

        for _ in range(10):
            interval_key = generator._choose_interval()
            self.assertIn(interval_key, generator.interval_files)
            self.assertNotIn('Flat', interval_key)

    @patch('simpleaudio.WaveObject.from_wave_file')
    @patch('simpleaudio.PlayObject')
    def test_minor_scale_flats(self, mock_wave_object, mock_play_object):
        scale = MinorScale('D', use_flats=True)  # D minor with flats
        generator = IntervalAudioGenerator(scale, bpm=60, use_extended=False, octave_preference='both')

        for _ in range(10):
            interval_key = generator._choose_interval()
            self.assertIn(interval_key, generator.interval_files)
            self.assertNotIn('Sharp', interval_key)

    @patch('simpleaudio.WaveObject.from_wave_file')
    @patch('simpleaudio.PlayObject')
    def test_low_octave_only(self, mock_wave_object, mock_play_object):
        scale = MajorScale('C', use_flats=True)
        generator = IntervalAudioGenerator(scale, bpm=60, use_extended=False, octave_preference='low')

        for _ in range(10):
            interval_key = generator._choose_interval()
            self.assertNotIn('low', interval_key)
            self.assertNotIn('high', interval_key)
            self.assertIn(interval_key, generator.interval_files)

    @patch('simpleaudio.WaveObject.from_wave_file')
    @patch('simpleaudio.PlayObject')
    def test_high_octave_only(self, mock_wave_object, mock_play_object):
        scale = MajorScale('C', use_flats=True)
        generator = IntervalAudioGenerator(scale, bpm=60, use_extended=False, octave_preference='high')

        for _ in range(10):
            interval_key = generator._choose_interval()
            self.assertNotIn('low', interval_key)
            self.assertNotIn('high', interval_key)
            self.assertIn(interval_key, generator.interval_files)

    @patch('simpleaudio.WaveObject.from_wave_file')
    @patch('simpleaudio.PlayObject')
    def test_both_octaves(self, mock_wave_object, mock_play_object):
        scale = MajorScale('C', use_flats=True)
        generator = IntervalAudioGenerator(scale, bpm=60, use_extended=False, octave_preference='both')

        seen_low = False
        seen_high = False
        for _ in range(20):
            interval_key = generator._choose_interval()
            self.assertIn(interval_key, generator.interval_files)
            if 'low' in interval_key:
                seen_low = True
            if 'high' in interval_key:
                seen_high = True

        self.assertTrue(seen_low or seen_high)  # Ensuring at least one of them is seen

    @patch('simpleaudio.WaveObject.from_wave_file')
    @patch('simpleaudio.PlayObject')
    def test_extended_range(self, mock_wave_object, mock_play_object):
        scale = MajorScale('C', use_flats=True)
        generator = IntervalAudioGenerator(scale, bpm=60, use_extended=True, octave_preference='both')

        for _ in range(10):
            interval_key = generator._choose_interval()
            self.assertTrue(interval_key[0].isdigit())
            self.assertIn(interval_key, generator.interval_files)

    @patch('simpleaudio.WaveObject.from_wave_file')
    @patch('simpleaudio.PlayObject')
    def test_no_accidentals(self, mock_wave_object, mock_play_object):
        scale = MajorScale('C', use_flats=True)
        generator = IntervalAudioGenerator(scale, bpm=60, use_extended=False, octave_preference='both')

        for _ in range(10):
            interval_key = generator._choose_interval()
            self.assertIn(interval_key, generator.interval_files)
            if 'Flat' not in interval_key and 'Sharp' not in interval_key:
                self.assertIn(interval_key, generator.interval_files)

    @patch('simpleaudio.WaveObject.from_wave_file')
    @patch('simpleaudio.PlayObject')
    def test_accidentals_only(self, mock_wave_object, mock_play_object):
        scale = MajorScale('C', use_flats=True)
        generator = IntervalAudioGenerator(scale, bpm=60, use_extended=False, octave_preference='both')

        generator.accidental_type = 'Flat'
        for _ in range(10):
            interval_key = generator._choose_interval()
            if 'Flat' in interval_key:
                self.assertIn(interval_key, generator.interval_files)

        generator.accidental_type = 'Sharp'
        for _ in range(10):
            interval_key = generator._choose_interval()
            if 'Sharp' in interval_key:
                self.assertIn(interval_key, generator.interval_files)

    @patch('simpleaudio.WaveObject.from_wave_file')
    def test_playing_files(self, mock_from_wave_file):
        scale = MajorScale('C', use_flats=True)
        generator = IntervalAudioGenerator(scale, bpm=60, use_extended=True, octave_preference='both')

        # Set up the mock for from_wave_file to return a mock wave object
        mock_wave_obj = MagicMock()
        mock_from_wave_file.return_value = mock_wave_obj

        # Mock the play method and the play object it returns
        mock_play_obj = MagicMock()
        mock_wave_obj.play.return_value = mock_play_obj

        # Run the method for a single iteration
        generator.generate_random_interval(iterations=1)

        # Verify that from_wave_file was called
        mock_from_wave_file.assert_called()
        # Verify that play was called on the wave object
        mock_wave_obj.play.assert_called()
        # Verify that wait_done was called on the play object
        mock_play_obj.wait_done.assert_called()

    @patch('simpleaudio.WaveObject.from_wave_file')
    def test_valid_intervals_c_major(self, mock_from_wave_file):
        # C major scale does not contain any sharps or flats
        scale = MajorScale('C', use_flats=False)
        generator = IntervalAudioGenerator(scale, bpm=60, use_extended=False, octave_preference='both')

        valid_intervals = {
            'low1', 'low2', 'low3', 'low4', 'low5', 'low6', 'low7',
            'high1', 'high2', 'high3', 'high4', 'high5', 'high6', 'high7'
        }

        for _ in range(100):  # Test multiple times to ensure randomness covers all cases
            interval_key = generator._choose_interval()
            # Remove accidental checks for C major as it shouldn't generate any
            interval_key_no_accidental = interval_key.replace('Flat', '').replace('Sharp', '')
            self.assertIn(interval_key_no_accidental, valid_intervals)
            self.assertNotIn('Flat', interval_key)
            self.assertNotIn('Sharp', interval_key)


    @patch('simpleaudio.WaveObject.from_wave_file')
    def test_valid_intervals_all_keys(self, mock_from_wave_file):
        # Define a list of all major keys and whether they use flats
        keys = [
            ('C', False),  # C major
            ('G', False),  # G major (1 sharp)
            ('D', False),  # D major (2 sharps)
            ('A', False),  # A major (3 sharps)
            ('E', False),  # E major (4 sharps)
            ('B', False),  # B major (5 sharps)
            ('F#', False), # F# major (6 sharps)
            ('C#', False), # C# major (7 sharps)
            ('F', True),   # F major (1 flat)
            ('Bb', True),  # Bb major (2 flats)
            ('Eb', True),  # Eb major (3 flats)
            ('Ab', True),  # Ab major (4 flats)
            ('Db', True),  # Db major (5 flats)
            ('Gb', True),  # Gb major (6 flats)
            ('Cb', True)   # Cb major (7 flats)
        ]

        for key, use_flats in keys:
            with self.subTest(key=key, use_flats=use_flats):
                scale = MajorScale(key, use_flats=use_flats)
                generator = IntervalAudioGenerator(scale, bpm=60, use_extended=False, octave_preference='both')

                # Define valid intervals without accidentals
                valid_intervals = {
                    'low1', 'low2', 'low3', 'low4', 'low5', 'low6', 'low7',
                    'high1', 'high2', 'high3', 'high4', 'high5', 'high6', 'high7'
                }

                for _ in range(100):  # Test multiple times to ensure randomness covers all cases
                    interval_key = generator._choose_interval()
                    # Remove accidental checks for C major as it shouldn't generate any
                    interval_key_no_accidental = interval_key.replace('Flat', '').replace('Sharp', '')
                    self.assertIn(interval_key_no_accidental, valid_intervals)
                    # Check for accidentals according to the scale
                    if not use_flats:
                        self.assertNotIn('Flat', interval_key)
                    else:
                        self.assertNotIn('Sharp', interval_key)



if __name__ == '__main__':
    unittest.main()
