from pydub import AudioSegment
from pydub.silence import split_on_silence
import os

def split_audio_on_silence(
    input_file,
    output_folder="output_chunks",
    min_silence_len=1000,  # milliseconds
    silence_thresh_db=-40,  # in dBFS
    keep_silence=300        # milliseconds
):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Split audio where silence is detected
    chunks = split_on_silence(
        audio,
        min_silence_len=min_silence_len,
        silence_thresh=audio.dBFS + silence_thresh_db,
        keep_silence=keep_silence
    )

    # Create output folder
    os.makedirs(output_folder, exist_ok=True)

    # Export each chunk as a separate file
    for i, chunk in enumerate(chunks):
        chunk_filename = os.path.join(output_folder, f"chunk_{i+1}.wav")
        chunk.export(chunk_filename, format="wav")
        print(f"Exported {chunk_filename}")

    print(f"Done! Exported {len(chunks)} chunks to '{output_folder}'")

# Example usage
split_audio_on_silence("example_audio.wav")
