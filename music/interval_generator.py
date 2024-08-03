import random
import time
import simpleaudio as sa

from music.scale import MajorScale, MinorScale

class IntervalAudioGenerator:
    interval_files = {
        'low1': 'audio/low1.wav',
        'low2': 'audio/low2.wav',
        'low3': 'audio/low3.wav',
        'low4': 'audio/low4.wav',
        'low5': 'audio/low5.wav',
        'low6': 'audio/low6.wav',
        'low7': 'audio/low7.wav',
        'high1': 'audio/high1.wav',
        'high2': 'audio/high2.wav',
        'high3': 'audio/high3.wav',
        'high4': 'audio/high4.wav',
        'high5': 'audio/high5.wav',
        'high6': 'audio/high6.wav',
        'high7': 'audio/high7.wav'
    }

    def __init__(self, scale, bpm):
        self.scale = scale
        self.bpm = bpm

    def generate_random_interval(self):
        """Continuously generates a random interval from the given scale every beat,
        where the tempo is defined by 'bpm' (beats per minute),
        and plays the corresponding audio file."""
        interval_seconds = 60 / self.bpm

        while True:
            octave_choice = random.choice(['low', 'high'])
            scale_degree = random.randint(1, 7)
            interval_key = f"{octave_choice}{scale_degree}"

            print(interval_key)  # For debugging or logging purposes

            try:
                wave_obj = sa.WaveObject.from_wave_file(self.interval_files[interval_key])
                play_obj = wave_obj.play()
                play_obj.wait_done()  # Wait for the audio to finish playing
            except Exception as e:
                print(f"Failed to play the interval: {e}")

            time.sleep(interval_seconds)

# Example usage:
if __name__ == "__main__":
    # Create a scale instance, e.g., a C major scale
    major = MajorScale('C', use_flats=True)

    # Create an IntervalAudioGenerator instance
    interval_generator = IntervalAudioGenerator(major, 15)

    # Start generating and playing intervals at 15 beats per minute
    interval_generator.generate_random_interval()
