import random
import time
import simpleaudio as sa
from music.scale import MajorScale, MinorScale

class IntervalAudioGenerator:
    interval_files = {
        # Files for standard octaves
        'low1': 'audio/Low1.wav',
        'low1Flat': 'audio/Low1Flat.wav',
        'low1Sharp': 'audio/Low1Sharp.wav',
        'low2': 'audio/Low2.wav',
        'low2Flat': 'audio/Low2Flat.wav',
        'low2Sharp': 'audio/Low2Sharp.wav',
        'low3': 'audio/Low3.wav',
        'low3Flat': 'audio/Low3Flat.wav',
        'low3Sharp': 'audio/Low3Sharp.wav',
        'low4': 'audio/Low4.wav',
        'low4Flat': 'audio/Low4Flat.wav',
        'low4Sharp': 'audio/Low4Sharp.wav',
        'low5': 'audio/Low5.wav',
        'low5Flat': 'audio/Low5Flat.wav',
        'low5Sharp': 'audio/Low5Sharp.wav',
        'low6': 'audio/Low6.wav',
        'low6Flat': 'audio/Low6Flat.wav',
        'low6Sharp': 'audio/Low6Sharp.wav',
        'low7': 'audio/Low7.wav',
        'low7Flat': 'audio/Low7Flat.wav',
        'low7Sharp': 'audio/Low7Sharp.wav',

        'high1': 'audio/High1.wav',
        'high1Flat': 'audio/High1Flat.wav',
        'high1Sharp': 'audio/High1Sharp.wav',
        'high2': 'audio/High2.wav',
        'high2Flat': 'audio/High2Flat.wav',
        'high2Sharp': 'audio/High2Sharp.wav',
        'high3': 'audio/High3.wav',
        'high3Flat': 'audio/High3Flat.wav',
        'high3Sharp': 'audio/High3Sharp.wav',
        'high4': 'audio/High4.wav',
        'high4Flat': 'audio/High4Flat.wav',
        'high4Sharp': 'audio/High4Sharp.wav',
        'high5': 'audio/High5.wav',
        'high5Flat': 'audio/High5Flat.wav',
        'high5Sharp': 'audio/High5Sharp.wav',
        'high6': 'audio/High6.wav',
        'high6Flat': 'audio/High6Flat.wav',
        'high6Sharp': 'audio/High6Sharp.wav',
        'high7': 'audio/High7.wav',
        'high7Flat': 'audio/High7Flat.wav',
        'high7Sharp': 'audio/High7Sharp.wav',

        # Files for extended range (1-16)
        '1': 'audio/1.wav',
        '1Flat': 'audio/1Flat.wav',
        '1Sharp': 'audio/1Sharp.wav',
        '2': 'audio/2.wav',
        '2Flat': 'audio/2Flat.wav',
        '2Sharp': 'audio/2Sharp.wav',
        '3': 'audio/3.wav',
        '3Flat': 'audio/3Flat.wav',
        '3Sharp': 'audio/3Sharp.wav',
        '4': 'audio/4.wav',
        '4Flat': 'audio/4Flat.wav',
        '4Sharp': 'audio/4Sharp.wav',
        '5': 'audio/5.wav',
        '5Flat': 'audio/5Flat.wav',
        '5Sharp': 'audio/5Sharp.wav',
        '6': 'audio/6.wav',
        '6Flat': 'audio/6Flat.wav',
        '6Sharp': 'audio/6Sharp.wav',
        '7': 'audio/7.wav',
        '7Flat': 'audio/7Flat.wav',
        '7Sharp': 'audio/7Sharp.wav',
        '8': 'audio/8.wav',
        '8Flat': 'audio/8Flat.wav',
        '8Sharp': 'audio/8Sharp.wav',
        '9': 'audio/9.wav',
        '9Flat': 'audio/9Flat.wav',
        '9Sharp': 'audio/9Sharp.wav',
        '10': 'audio/10.wav',
        '10Flat': 'audio/10Flat.wav',
        '10Sharp': 'audio/10Sharp.wav',
        '11': 'audio/11.wav',
        '11Flat': 'audio/11Flat.wav',
        '11Sharp': 'audio/11Sharp.wav',
        '12': 'audio/12.wav',
        '12Flat': 'audio/12Flat.wav',
        '12Sharp': 'audio/12Sharp.wav',
        '13': 'audio/13.wav',
        '13Flat': 'audio/13Flat.wav',
        '13Sharp': 'audio/13Sharp.wav',
        '14': 'audio/14.wav',
        '14Flat': 'audio/14Flat.wav',
        '14Sharp': 'audio/14Sharp.wav',
        '15': 'audio/15.wav',
        '15Flat': 'audio/15Flat.wav',
        '15Sharp': 'audio/15Sharp.wav',
        '16': 'audio/16.wav',
        '16Flat': 'audio/16Flat.wav',
        '16Sharp': 'audio/16Sharp.wav'
    }

    def __init__(self, scale, bpm, use_extended=False, octave_preference='both'):
        self.scale = scale
        self.bpm = bpm
        self.use_extended = use_extended
        self.octave_preference = octave_preference
        self.accidental_type = 'Flat' if scale.use_flats else 'Sharp'

    def generate_random_interval(self, iterations=None):
        """Generates a random interval from the given scale every beat,
        playing the corresponding audio file."""
        interval_seconds = 60 / self.bpm
        count = 0

        while True:
            interval_key = self._choose_interval()
            print(interval_key)  # For debugging or logging purposes

            try:
                wave_obj = sa.WaveObject.from_wave_file(self.interval_files[interval_key])
                play_obj = wave_obj.play()
                play_obj.wait_done()  # Wait for the audio to finish playing
            except Exception as e:
                print(f"Failed to play the interval: {e}")

            time.sleep(interval_seconds)

            count += 1
            if iterations is not None and count >= iterations:
                break

    def _choose_interval(self):
        """Choose a random interval based on the current configuration."""
        scale_degree = random.randint(1, 16 if self.use_extended else 7)

        if self.use_extended:
            # For extended ranges, consider accidentals if applicable
            accidental_type = '' if self.scale.use_flats is None else self.accidental_type
            return f"{scale_degree}{accidental_type}"

        # Determine if accidentals should be considered for non-extended range
        if not self.scale.use_flats and self.scale.root not in self.scale.FLAT_KEYS:
            accidental_type = ''  # No accidentals for C major or other natural scales
        else:
            if self.scale.root in self.scale.SHARP_KEYS and not self.scale.use_flats:
                accidental_type = 'Sharp'
            elif self.scale.root in self.scale.FLAT_KEYS and self.scale.use_flats:
                accidental_type = 'Flat'
            else:
                accidental_type = ''  # No accidentals for natural scales

        # Choose the correct interval key based on octave preference
        if self.octave_preference == 'both':
            octave_choice = random.choice(['low', 'high'])
            return f"{octave_choice}{scale_degree}{accidental_type}"
        else:
            # For low or high preference, use only the basic intervals (1-7)
            return f"{scale_degree}{accidental_type}"


# Example usage:
if __name__ == "__main__":
    # Create a scale instance, e.g., a C major scale
    major = MajorScale('F', use_flats=True)

    # Create an IntervalAudioGenerator instance with extended range and specific octave preference
    interval_generator = IntervalAudioGenerator(major, 30, use_extended=False, octave_preference='low')

    # Start generating and playing intervals at 15 beats per minute
    interval_generator.generate_random_interval()
