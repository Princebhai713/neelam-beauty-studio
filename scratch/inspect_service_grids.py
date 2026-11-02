from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

services_sec = [s for s in soup.find_all('section') if 'Feel the Difference' in s.get_text()][0]
grids = services_sec.find_all('div', class_=lambda c: c and 'grid' in c)
print('Grids count:', len(grids))
for i, g in enumerate(grids):
    children = g.find_all(recursive=False)
    print(f'Grid {i}: class={g.get("class")}, direct children={len(children)}')
    for c in children:
        title = c.find(['h3', 'h4', 'h5'])
        t_text = title.get_text(strip=True) if title else 'No title'
        print(f'   - {t_text}')
