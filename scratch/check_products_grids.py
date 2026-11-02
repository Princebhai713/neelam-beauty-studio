from bs4 import BeautifulSoup
import re

with open('products.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace cards-grid-3 for featured products with featured-products-grid
# Replace cards-grid-3 for categories with categories-grid-6
# Replace trust grid with trust-badges-grid-6

soup = BeautifulSoup(text, 'html.parser')

# Let's inspect sections
sections = soup.find_all('section')
for s in sections:
    h2 = s.find('h2')
    if h2:
        grid = s.find('div', class_=lambda c: c and 'grid' in c)
        print(f'{h2.get_text(strip=True)} -> Grid: {grid.get("class") if grid else "No grid"}')
