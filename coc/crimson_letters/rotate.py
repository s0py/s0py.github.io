import os
from PIL import Image
import random

# Get all image files in current directory
image_extensions = ('.png')
image_files = [f for f in os.listdir('.') if f.lower().endswith(image_extensions)]

for image_file in image_files:
    print(f"Processing: {image_file}")
    input_text = input(f"Press Enter to rotate {image_file} randomly, or any other key to skip: ")
    
    if input_text == "":
        # Open and rotate image
        with Image.open(image_file) as img:
            # Random rotation between -2 and 2 degrees
            rotation = random.uniform(-2, 2)
            rotated = img.rotate(rotation, expand=True, resample=Image.BICUBIC, fillcolor=None)
            
            # Save with '_rotated' suffix
            filename, ext = os.path.splitext(image_file)
            new_filename = f"{filename}{ext}"
            rotated.save(new_filename)
            print(f"Saved as: {new_filename}")
    else:
        print("Skipped")