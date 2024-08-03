from music.music_generator import MusicGenerator
from music.scale import MajorScale, MinorScale

# Example usage:
if __name__ == "__main__":
    # Create a scale instance, e.g., a C major scale
    major = MajorScale('C', use_flats=True)
    minor = MinorScale('D', use_flats=True)
    # Create a MusicGenerator instance
    generator = MusicGenerator(major, 15)

    # Start generating and playing notes at 15 beats per minute
    generator.generate_random_note_from_scale()
