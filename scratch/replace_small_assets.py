import os
from PIL import Image

replacements = {
    'body-side-model.png': 'assets/images/ba-bodyskin.png',
    'hair-cta-model.png': 'assets/images/avatar-sneha.png',
    'hair-side-model.png': 'assets/images/avatar-pooja.png',
    'home-about-5.png': 'assets/images/avatar-priya.png',
    'services-side-academy.png': 'assets/images/acad-moment-1.png',
    'services-side-special.png': 'assets/images/spec-g-1.png',
    'spec-g-7.png': 'assets/images/spec-g-2.png',
    'srv-dandiya.png': 'assets/images/srv-costume.png',
}

for target, source in replacements.items():
    target_path = os.path.join('assets/images', target)
    if os.path.exists(source):
        im = Image.open(source)
        im.save(target_path)
        print(f'Replaced {target} with {source} -> size: {im.size}')
    else:
        print(f'Source {source} not found!')
