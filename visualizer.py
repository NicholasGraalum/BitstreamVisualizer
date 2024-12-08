#!/usr/bin/env python3
from PIL import Image
import numpy as np
import sys

def binary_to_bitsream(binaryfile, sizes):

    # Make the ouptut name the name of the binaryfile being processed

    # Open the binary file as read
    with open(binaryfile, 'r') as f:
        lines = f.read()
    
    # Remove all spaces from the binary file
    binary_data = "".join(char for line in lines for char in line.strip() if char in "01")

    # Convert the data to a numpy array
    bit_array = np.array([int(bit) for bit in binary_data], dtype=np.uint8)

    for width, height in sizes:
        # Generate a name for the image based on the sizes of the image
        output_file = f"{binaryfile}_{width}X{height}_output.png"
        total_pixels = width * height

        # Reshape the array to fit the dimensions of the image
        if len(bit_array) < total_pixels:
            padded_array = np.pad(bit_array, (0, width * height - len(bit_array)), mode='constant', constant_values=0)
        else:
            padded_array = bit_array[:total_pixels]
        
        reshaped_array = padded_array.reshape((height, width))

        # Create the image and save it under the output file name
        img = Image.fromarray(reshaped_array * 255, mode='L')
        img.save(output_file)

    return

if __name__ == '__main__':
    sizes = [(1024, 1024), (512, 512), (128, 128), (20, 80)]
    binary_to_bitsream(sys.argv[1], sizes)
