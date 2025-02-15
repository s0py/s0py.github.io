import os
from PIL import Image
import random

# Get all image files in current directory
image_extensions = ('.png')
image_files = [f for f in os.listdir('.') if f.lower().endswith(image_extensions)]

for image_file in image_files:
    print(f"Processing: {image_file}")
    # Open and rotate image
    with Image.open(image_file) as img:
        # Save with '_rotated' suffix
        filename, ext = os.path.splitext(image_file)
        new_filename = f"{filename}.webp"
        img.save(new_filename, 'webp', optimize = True, quality = 100)
        print(f"Saved as: {new_filename}")