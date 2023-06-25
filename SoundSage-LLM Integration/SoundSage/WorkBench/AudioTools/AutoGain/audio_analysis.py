import librosa
import numpy as np
from pyloudnorm import Meter


def analyze_audio(audio_file):
    y, sr = librosa.load(audio_file, sr=None)  # Added `sr=None` to avoid resampling
    meter = Meter(sr)
    lufs = meter.integrated_loudness(y)

    # Compute the maximum decibels full scale (dBFS) and subtract the headroom
    max_dbfs = np.max(librosa.amplitude_to_db(y)) - 18  # Subtract the headroom

    # Compute the number of bits per sample
    bits_per_sample = y.dtype.itemsize * 8

    # Compute the number of audio channels (1 for mono, 2 for stereo)
    num_channels = 1 if len(y.shape) == 1 else y.shape[1]

    return {'lufs': lufs, 'max_dbfs': max_dbfs, 'bits_per_sample': bits_per_sample, 'num_channels': num_channels}
