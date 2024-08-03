from music.music_generator import MusicGenerator
from music.scale import MajorScale, MinorScale

# Example usage:
if __name__ == "__main__":
    # Create a scale instance, e.g., a C major scale
    major = MajorScale('D', use_flats=False)
    minor = MinorScale('D', use_flats=True)

    # Create a MusicGenerator instance
    generator = MusicGenerator(minor, 15 )

    # Start generating and playing chords at 15 beats per minute
    generator.generate_random_chord_from_scale()
