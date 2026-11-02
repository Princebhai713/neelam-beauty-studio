with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx1 = text.find('cards-grid-4')
# find the opening <div of cards-grid-4
start_tag = text.rfind('<div', 0, idx1)

# find the closing </div> of that grid before Explore All Services
end_marker = 'Explore All Services'
end_tag = text.rfind('</div>', 0, text.find(end_marker))

print('Found start_tag at:', start_tag, 'end_tag at:', end_tag)

services_16_html = '''<div class="services-grid-8" style="margin-bottom: 28px;">
        <!-- 1. Bridal Makeup -->
        <a href="bridal-makeup.html" class="service-card-compact">
          <div class="card-media"><img src="assets/images/srv-bridal.png" alt="Bridal Makeup"></div>
          <div class="card-info">
            <h4>Bridal Makeup</h4>
            <p>Royal bridal looks</p>
          </div>
        </a>

        <!-- 2. Bridal Video Shoot -->
        <a href="bridal-makeup.html#video" class="service-card-compact">
          <div class="card-media"><img src="assets/images/srv-video.png" alt="Bridal Video Shoot"></div>
          <div class="card-info">
            <h4>Bridal Video Shoot</h4>
            <p>Cinematic HD session</p>
          </div>
        </a>

        <!-- 3. General Makeup -->
        <a href="services.html" class="service-card-compact">
          <div class="card-media"><img src="assets/images/srv-general.png" alt="General Makeup"></div>
          <div class="card-info">
            <h4>General Makeup</h4>
            <p>Celebration makeup</p>
          </div>
        </a>

        <!-- 4. Skin Care (Facial & Clean Up) -->
        <a href="skin-care.html" class="service-card-compact">
          <div class="card-media"><img src="assets/images/srv-skincare.png" alt="Skin Care"></div>
          <div class="card-info">
            <h4>Skin Care</h4>
            <p>Facial & Clean Up</p>
          </div>
        </a>

        <!-- 5. Body Care -->
        <a href="hair-body-care.html#body" class="service-card-compact">
          <div class="card-media"><img src="assets/images/srv-bodycare.png" alt="Body Care"></div>
          <div class="card-info">
            <h4>Body Care</h4>
            <p>Polishing & Spa</p>
          </div>
        </a>

        <!-- 6. Hair Care -->
        <a href="hair-body-care.html" class="service-card-compact">
          <div class="card-media"><img src="assets/images/srv-haircare.png" alt="Hair Care"></div>
          <div class="card-info">
            <h4>Hair Care</h4>
            <p>Keratin & Botox</p>
          </div>
        </a>

        <!-- 7. Ear Lobbying -->
        <a href="special-services.html#earlobe" class="service-card-compact">
          <div class="card-media"><img src="assets/images/srv-earlob.png" alt="Ear Lobbying"></div>
          <div class="card-info">
            <h4>Ear Lobbying</h4>
            <p>Non-surgical repair</p>
          </div>
        </a>

        <!-- 8. Tataoo -->
        <a href="special-services.html#tattoo" class="service-card-compact">
          <div class="card-media"><img src="assets/images/srv-tattoo.png" alt="Tataoo"></div>
          <div class="card-info">
            <h4>Tataoo</h4>
            <p>Hygienic artistic ink</p>
          </div>
        </a>

        <!-- 9. Ear Piercing -->
        <a href="special-services.html#piercing" class="service-card-compact">
          <div class="card-media"><img src="assets/images/srv-earpiercing.png" alt="Ear Piercing"></div>
          <div class="card-info">
            <h4>Ear Piercing</h4>
            <p>Painless gun/needle</p>
          </div>
        </a>

        <!-- 10. Hydra Facial -->
        <a href="skin-care.html" class="service-card-compact">
          <div class="card-media"><img src="assets/images/srv-hydra.png" alt="Hydra Facial"></div>
          <div class="card-info">
            <h4>Hydra Facial</h4>
            <p>Deep pore glow</p>
          </div>
        </a>

        <!-- 11. Carbon Laser Treatment -->
        <a href="skin-care.html#laser" class="service-card-compact">
          <div class="card-media"><img src="assets/images/srv-carbon.png" alt="Carbon Laser"></div>
          <div class="card-info">
            <h4>Carbon Laser Treatment</h4>
            <p>Pore tightening</p>
          </div>
        </a>

        <!-- 12. Costume Makeup -->
        <a href="special-services.html" class="service-card-compact">
          <div class="card-media"><img src="assets/images/srv-costume.png" alt="Costume Makeup"></div>
          <div class="card-info">
            <h4>Costume Makeup</h4>
            <p>Dandiya / Party</p>
          </div>
        </a>

        <!-- 13. Mehandi -->
        <a href="special-services.html#mehndi" class="service-card-compact">
          <div class="card-media"><img src="assets/images/srv-mehandi.png" alt="Mehandi"></div>
          <div class="card-info">
            <h4>Mehandi</h4>
            <p>Bridal henna artistry</p>
          </div>
        </a>

        <!-- 14. All Skin & Hair Care -->
        <a href="hair-body-care.html" class="service-card-compact">
          <div class="card-media"><img src="assets/images/srv-allskinhair.png" alt="All Skin & Hair Care"></div>
          <div class="card-info">
            <h4>All Skin & Hair Care</h4>
            <p>Kreton & More</p>
          </div>
        </a>

        <!-- 15. Facials & Clean Up -->
        <a href="skin-care.html" class="service-card-compact">
          <div class="card-media"><img src="assets/images/srv-facials.png" alt="Facials & Clean Up"></div>
          <div class="card-info">
            <h4>Facials & Clean Up</h4>
            <p>Organic fruit facials</p>
          </div>
        </a>

        <!-- 16. And Many More... (Special Card) -->
        <a href="services.html" class="service-card-compact special-more">
          <span>And Many More...</span>
        </a>
      </div>'''

new_text = text[:start_tag] + services_16_html + text[end_tag+len('</div>'):]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print('Successfully inserted 16 service cards into index.html!')
