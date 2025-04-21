import sys
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

# File extensions to include
SUPPORTED_EXTENSIONS = ('.wav', '.mp3', '.flac', '.ogg', '.m4a')

def split_audio_on_silence(
    input_file,
    output_folder,
    min_silence_len=1000,
    silence_thresh_db=-40,
    keep_silence=300
):
    audio = AudioSegment.from_file(input_file)
    chunks = split_on_silence(
        audio,
        min_silence_len=min_silence_len,
        silence_thresh=audio.dBFS + silence_thresh_db,
        keep_silence=keep_silence
    )

    os.makedirs(output_folder, exist_ok=True)

    for i, chunk in enumerate(chunks):
        chunk_filename = os.path.join(output_folder, f"slice_{i+1}.wav")
        chunk.export(chunk_filename, format="wav")
        print(f"Exported {chunk_filename}")

    print(f"Done! Exported {len(chunks)} chunks for '{input_file}'\n")

def process_audio_folder(input_folder, output_base="output_slices"):
    if not os.path.isdir(input_folder):
        print(f"Error: '{input_folder}' is not a valid folder.")
        return

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(SUPPORTED_EXTENSIONS):
            input_path = os.path.join(input_folder, filename)
            output_folder = os.path.join(output_base, os.path.splitext(filename)[0] + "_slices")
            print(f"Processing: {input_path}")
            split_audio_on_silence(input_path, output_folder)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pyslice.py <path_to_audio_folder>")
        sys.exit(1)

    input_folder = sys.argv[1]
    process_audio_folder(input_folder)

