import matplotlib.pyplot as plt
import numpy as np
import os
from pydub import AudioSegment

import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
from scipy.signal import find_peaks

def load_audio(file_path):
    """Load an audio file using PyDub and convert to numpy array."""
    audio = AudioSegment.from_file(file_path)
    data = np.array(audio.get_array_of_samples())
    if audio.channels == 2:
        data = data.reshape((-1, 2)).sum(axis=1)
    return data, audio.frame_rate

def detect_peaks(data):
    """Detect peaks in the audio data."""
    peaks, _ = find_peaks(data, height=np.max(data)*0.5)  # Adjust height as needed
    return peaks

def calculate_beat_times(duration, bpm=100):
    """Calculate the times for each beat based on BPM."""
    beat_time = 60 / bpm
    return np.arange(0, duration, beat_time)

def find_closest_peaks(peaks, beat_times, sr):
    """Find the closest peak to each beat."""
    peak_times = peaks / sr
    closest_peaks = []
    for beat in beat_times:
        idx = (np.abs(peak_times - beat)).argmin()
        closest_peaks.append(peak_times[idx])
    return closest_peaks

def plot_waveform_with_peaks(data, sr, peaks, beat_times, closest_peaks):
    """Plot the waveform, peaks, and closest peaks to beats."""
    plt.figure(figsize=(14, 5))
    times = np.arange(0, len(data)) / sr
    plt.plot(times, data, label='Waveform')
    plt.plot(peaks/sr, data[peaks], "x", label='Peaks')
    for beat in beat_times:
        plt.axvline(x=beat, color='blue', linestyle='--', linewidth=0.5)
    for peak in closest_peaks:
        plt.axvline(x=peak, color='red', linestyle='-', linewidth=2)
    plt.title('Waveform with Beats and Closest Peaks')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.savefig('waveform.png')

def analyze_timing_errors(beat_times, closest_peaks):
    """Analyze timing errors and provide statistics."""
    data = closest_peaks - beat_times

    # Scatter plot of individual errors
    fig, ax = plt.subplots()
    ax.scatter(beat_times, data, color='red', label='Timing Errors')
    ax.axhline(y=0, color='blue', linestyle='-', label='Metronome')

    # Adding labels and title
    ax.set_xlabel('Beat Times (s)')
    ax.set_ylabel('Timing Errors (s)')
    ax.set_title('Timing Errors Scatter Plot')
    ax.legend()

    mean_error = np.mean(data)
    std_deviation = np.std(data)

    data_before = data[data < 0]
    data_after = data[data >= 0]
    mean_data_before = np.mean(data_before) if data_before.size > 0 else 0
    mean_data_after = np.mean(data_after) if data_after.size > 0 else 0
    std_before = np.std(data_before)
    std_after = np.std(data_after)

    plt.savefig("barchaart.png")
    return data, mean_error, std_deviation, mean_data_before, mean_data_after

def main():
    # Update these paths to where you saved your exported audio files
    this_dir = os.path.dirname(os.path.abspath(__file__))
    metronome_file_path = os.path.join(this_dir, "TimingExercise Metronome.flac")
    guitar_file_path = os.path.join(this_dir, "TimingExercise Guitar.flac")

    data, sr = load_audio(guitar_file_path)
    peaks = detect_peaks(data)
    duration = len(data) / sr
    beat_times = calculate_beat_times(duration, bpm=100)
    closest_peaks = find_closest_peaks(peaks, beat_times, sr)

    errors, mean_error, std_deviation, mean_error_before, mean_error_after = analyze_timing_errors(beat_times, closest_peaks)


if __name__ == "__main__":
    main()
