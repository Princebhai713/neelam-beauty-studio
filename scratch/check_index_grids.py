from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# Check quick icons
quick_grid = soup.find('div', class_='quick-icons-grid')
if quick_grid:
    cards = quick_grid.find_all('a', class_='quick-icon-card')
    print('Quick icons count in index.html:', len(cards))

# Check services grid
services_sec = None
for s in soup.find_all('section'):
    if 'Feel the Difference' in s.get_text():
        services_sec = s
        break

if services_sec:
    grid = services_sec.find('div', class_=lambda c: c and ('grid' in c))
    print('Services grid class:', grid.get('class') if grid else 'None')
    if grid:
        cards = grid.find_all('div', class_=lambda c: c and 'card' in c)
        print('Services cards count:', len(cards))
