import os
from PIL import Image

for f in sorted(os.listdir('assets/images')):
    if f.endswith(('.png', '.jpg', '.webp')):
        try:
            im = Image.open(os.path.join('assets/images', f))
            print(f'{f}: {im.size} {im.format}')
        except Exception as e:
            print(f'{f}: error {e}')
