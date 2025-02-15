import os
from PIL import Image

with Image.open("home - cecil hunter commit.webp") as img:
    # Save with '_rotated' suffix
    new_filename = f"home - cecil hunter commit - small - 90.webp"
    img.thumbnail([1000,1600],Image.LANCZOS)
    img.save(new_filename, 'webp', optimize = True, quality = 90)
    print(f"Saved as: {new_filename}")