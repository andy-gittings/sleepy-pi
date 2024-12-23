#!/usr/bin/env python3
#
#
# Play random audio files from /audio directory
#
#

import os, random, subprocess

def pick_random_file(directory):
    """
    Pick a random file from the specified directory hierarchy.

    Parameters:
        directory (str): The path to the directory to search for files.

    Returns:
        str: The path to the randomly selected file, or None if no files are found.
    """
    file_list = []

    # Walk through the directory hierarchy
    for root, _, files in os.walk(directory):
        for file in files:
            # Append the full file path to the list
            file_list.append(os.path.join(root, file))

    # Return a random file if the list is not empty
    if file_list:
        return random.choice(file_list)
    else:
        return None

def play_audio_file(file_path):
    """
    Play the audio file using cvlc player.

    Parameters:
        file_path (str): The path to the audio file to play.
    """
    try:
        subprocess.run(["cvlc", "--play-and-exit", file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error playing file: {e}")


if __name__ == "__main__":
    # Specify audio file location
    directory="/audio"

    #
    # Forever loop
    while 1:
        # Pick a random file
        random_file = pick_random_file(directory)

        # If a file was picked, play it using cvlc...
        if random_file:
                play_audio_file(random_file)
