import random
import time
import pyttsx3
import simpleaudio as sa

from music.scale import MajorScale


class IntervalGenerator:
    interval_files = {
        '1': 'audio/1.wav',
        'b1': 'audio/Flat1.wav',
        '#1': 'audio/Sharp1.wav',
        '2': 'audio/2.wav',
        'b2': 'audio/Flat2.wav',
        '#2': 'audio/Sharp2.wav',
        '3': 'audio/3.wav',
        'b3': 'audio/Flat3.wav',
        '#3': 'audio/Sharp3.wav',
        '4': 'audio/4.wav',
        'b4': 'audio/Flat4.wav',
        '#4': 'audio/Sharp4.wav',
        '5': 'audio/5.wav',
        'b5': 'audio/Flat5.wav',
        '#5': 'audio/Sharp5.wav',
        '6': 'audio/6.wav',
        'b6': 'audio/Flat6.wav',
        '#6': 'audio/Sharp6.wav',
        '7': 'audio/7.wav',
        'b7': 'audio/Flat7.wav',
        '#7': 'audio/Sharp7.wav',
    }

    def __init__(self, scale, bpm):
        self.scale = scale
        self.bpm = bpm
        # self.engine = pyttsx3.init()

    def generate_random_interval_from_scale(self):
        """Continuously generates a random interval from the given scale every beat,
        where the tempo is defined by 'bpm'(beats per minute),
        and plays the corresponding audio file."""
        print(f"Generating random intervals for: \"{self.scale}\"")
        interval_seconds = 60 / self.bpm

        while True:
            interval = random.choice(self.scale.get_intervals())
            print("Interval: ", interval, "; Note: ", (self.scale.build_scale()[self.scale.get_intervals().index(interval)]))
            try:
                # self.engine.say(interval)
                # self.engine.runAndWait()
                wave_obj = sa.WaveObject.from_wave_file(self.interval_files[interval])
                play_obj = wave_obj.play()
                play_obj.wait_done()  # Wait for the audio to finish playing
            except Exception as e:
                print(f"Failed to play the interval: {e}")
            time.sleep(interval_seconds)

    def generate_random_interval_sequence(self, lower_bound, upper_bound):
        """Generates and plays a random sequence of intervals from the scale.

        Arguments:
        lower_bound -- minimum number of intervals in a sequence
        upper_bound -- maximum number of intervals in a sequence
        """
        interval_seconds = 60 / self.bpm

        while True:
            sequence_length = random.randint(lower_bound, upper_bound)
            sequence = random.sample(self.scale.get_intervals(), sequence_length)
            print("Sequence:", sequence)

            for interval in sequence:
                try:
                    wave_obj = sa.WaveObject.from_wave_file(self.interval_files[interval])
                    play_obj = wave_obj.play()
                    play_obj.wait_done()  # Wait for the audio to finish playing
                except Exception as e:
                    print(f"Failed to play the interval: {e}")
            time.sleep(interval_seconds)

# Example usage:
if __name__ == "__main__":
    # Create a scale instance, e.g., a C major scale
    major = MajorScale('C', use_flats=False)
    # Create an IntervalGenerator instance
    generator = IntervalGenerator(major, 15)
    # Start generating and playing intervals at 15 beats per minute
    generator.generate_random_interval_sequence(1, 4)
