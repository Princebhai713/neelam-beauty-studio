with open('products.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('class="services-grid-6"', 'class="cards-grid-6"')

with open('products.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated products.html to use cards-grid-6!')
