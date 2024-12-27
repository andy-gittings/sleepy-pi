#!/usr/bin/env python3
#
#
# Play random audio files from /audio directory and handle airplay interruptions
#
#
import os
import random
import subprocess
import time

def get_audio_files_by_directory(directory):
    """
    Create a dictionary of audio files grouped by top-level subdirectories, excluding the top-level directory itself.

    Parameters:
        directory (str): The path to the directory to search for files.

    Returns:
        dict: A dictionary where keys are top-level subdirectories, and values are lists of audio file paths.
    """
    audio_files = {}
    audio_extensions = {".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"}

    for root, _, files in os.walk(directory):
        # Get the relative top-level directory
        relative_root = os.path.relpath(root, directory)
        if relative_root == ".":
            continue  # Skip the top-level directory itself
        top_level_dir = relative_root.split(os.sep)[0]

        if top_level_dir not in audio_files:
            audio_files[top_level_dir] = []

        for file in files:
            if os.path.splitext(file)[1].lower() in audio_extensions:
                audio_files[top_level_dir].append(os.path.join(root, file))

    return audio_files

def play_audio_file(file_path):
    """
    Play the audio file using cvlc player.

    Parameters:
        file_path (str): The path to the audio file to play.
    """
    process = None
    try:
        process = subprocess.Popen(["cvlc", "--play-and-exit", file_path])
        while process.poll() is None:
            if os.path.exists(control_file):
                process.terminate()
                process.wait()
                break
            time.sleep(5)
    except Exception as e:
        print(f"Error playing file: {e}")
    finally:
        if process and process.poll() is None:
            process.terminate()

if __name__ == "__main__":
    # Specify the root directory to search
    directory = "/audio"

    # Path to the airplay control file
    control_file = "/tmp/airplay-playing"

    # Get the audio files grouped by top-level subdirectories
    audio_files_by_directory = get_audio_files_by_directory(directory)

    # Continuously randomize the order of top-level directories and play a random file from each
    while True:
        if os.path.exists(control_file):
            time.sleep(5)  # Wait and check again
            continue

        top_level_dirs = list(audio_files_by_directory.keys())
        random.shuffle(top_level_dirs)
        for top_level_dir in top_level_dirs:
            files = audio_files_by_directory[top_level_dir]
            if files:
                random_file = random.choice(files)
                if not os.path.exists(control_file):
                    play_audio_file(random_file)
                else:
                    print("Airplay control file detected. Stopping playback.")
                    break
