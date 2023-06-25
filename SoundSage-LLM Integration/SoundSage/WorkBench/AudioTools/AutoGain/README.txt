
## AutoGain

AutoGain is the first tool integrated into the SoundSage system.
It automates the process of gain staging, setting the clip gain level to industry standards and ensuring a consistent
output for all users.
AutoGain works by taking input from the user regarding where the audio files are and where the user wants the
processed audio files to be designated for export.

### Modules and Functions

- `audio_analysis.py`: Analyzes the audio prior to processing.
- `audio_processor.py`: Processes the audio based on the analysis.

## Future Tools

SoundSage plans to integrate more tools for automated audio processing, including:

- AutoEQ
- AutoCompressor
- AutoLimiter
- AutoReverb
- AutoDelay
- AutoNoise Reduction
- AutoEnhancer
- AutoStereo Widener
- AutoPitch Corrector
- AutoTime Stretcher

## User Interface

AutoGain has a simple UI for choosing files and the intended destination directory and a button to click to begin processing.
