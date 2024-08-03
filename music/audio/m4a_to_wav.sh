#!/bin/bash

# Loop through all .m4a files in the current directory
for f in *.m4a; do
    # Convert the .m4a file to .wav
    ffmpeg -i "$f" "${f%.m4a}.wav"
    
    # Check if the conversion was successful
    if [ $? -eq 0 ]; then
        # Delete the original .m4a file
        rm "$f"
    else
        echo "Failed to convert $f"
    fi
done
