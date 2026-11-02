from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from PIL import Image

opts = Options()
opts.add_argument('--headless')
opts.add_argument('--window-size=1440,900')
driver = webdriver.Chrome(options=opts)

# Test products.html
driver.get('http://localhost:5500/products.html')
p_header = driver.find_element(By.CSS_SELECTOR, '.main-header, .site-header')
p_cont = p_header.find_element(By.CLASS_NAME, 'container')
p_logo = driver.find_element(By.CLASS_NAME, 'brand-logo')

print('=== PRODUCTS.HTML MEASUREMENTS ===')
print('Window innerWidth:', driver.execute_script('return window.innerWidth'))
print('Header rect:', p_header.rect)
print('Container rect:', p_cont.rect)
print('Logo rect:', p_logo.rect)

driver.save_screenshot('scratch/verified_products_1440.png')

# Test index.html
driver.get('http://localhost:5500/index.html')
i_header = driver.find_element(By.CSS_SELECTOR, '.main-header, .site-header')
i_cont = i_header.find_element(By.CLASS_NAME, 'container')
i_logo = driver.find_element(By.CLASS_NAME, 'brand-logo')

print('=== INDEX.HTML MEASUREMENTS ===')
print('Header rect:', i_header.rect)
print('Container rect:', i_cont.rect)
print('Logo rect:', i_logo.rect)

driver.save_screenshot('scratch/verified_index_1440.png')

driver.quit()

# Crop top 650px of both screenshots for direct viewing
p_im = Image.open('scratch/verified_products_1440.png')
p_im.crop((0, 0, p_im.size[0], 650)).save('scratch/verified_products_crop.png')

i_im = Image.open('scratch/verified_index_1440.png')
i_im.crop((0, 0, i_im.size[0], 650)).save('scratch/verified_index_crop.png')

print('Saved verified crops successfully!')
