import re

with open('products.html', 'r', encoding='utf-8') as f:
    text = f.read()

imgs = re.findall(r'<img [^>]*src=["\']([^"\']+)["\']', text)
for i, src in enumerate(imgs[:15]):
    print(f'{i+1}: {src}')
