import os
import ffmpy
import shutil
import subprocess
import json
def process_audio(audio_file, analyzed_data, output_directory):
    target_lufs = -18
    headroom = 18

    gain_adjustment = target_lufs - analyzed_data['lufs']
    output_file = os.path.join(output_directory, 'processed_' + os.path.basename(audio_file))

    # Get the input file's bits per sample and sample rate
    ffprobe = ffmpy.FFprobe(
        inputs={audio_file: None},
        global_options='-v error -show_entries stream=bits_per_sample,sample_rate -of json'
    )
    ffprobe_output = ffprobe.run(stdout=subprocess.PIPE)[0].decode()
    ffprobe_json = json.loads(ffprobe_output)
    bits_per_sample = int(ffprobe_json['streams'][0]['bits_per_sample'])
    sample_rate = int(ffprobe_json['streams'][0]['sample_rate'])

    # Set the output sample format based on the input bits per sample
    sample_format = {16: 'pcm_s16le', 32: 'pcm_s32le'}.get(bits_per_sample, 'pcm_s16le')

    if gain_adjustment != 0 or analyzed_data['max_dbfs'] > target_lufs + headroom:
        # Apply gain adjustment and set the output sample format
        ff = ffmpy.FFmpeg(
            inputs={audio_file: None},
            outputs={
                output_file: f'-ar {sample_rate} -acodec {sample_format} -af volume={gain_adjustment}dB'}
        )
        ff.run()

    else:
        # No processing needed, just copy the input file to the output file
        shutil.copyfile(audio_file, output_file)


