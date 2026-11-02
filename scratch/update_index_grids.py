import re

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# 1. Update Quick Icons to full 16 in 2 rows of 8 inside .quick-icons-box
quick_icons_16 = '''<section class="quick-icons-section">
    <div class="container">
      <div class="quick-icons-box">
        <div class="quick-icons-grid">
          <a href="beauty-academy.html" class="quick-icon-card">
            <div class="quick-icon-circle">
              <svg width="22" height="22" fill="currentColor" viewBox="0 0 24 24"><path d="M5 13.18v4L12 21l7-3.82v-4L12 17l-7-3.82zM12 3L1 9l11 6 9-4.91V17h2V9L12 3z"/></svg>
            </div>
            <span>Beauty Courses & Classes</span>
          </a>
          <a href="beauty-academy.html#online" class="quick-icon-card">
            <div class="quick-icon-circle">
              <svg width="22" height="22" fill="currentColor" viewBox="0 0 24 24"><path d="M20 18c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2H4c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2H0v2h24v-2h-4zM4 6h16v10H4V6z"/></svg>
            </div>
            <span>Online & Offline Classes</span>
          </a>
          <a href="bridal-makeup.html" class="quick-icon-card">
            <div class="quick-icon-circle">
              <svg width="22" height="22" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm0 14.2c-2.5 0-4.71-1.28-6-3.22.03-1.99 4-3.08 6-3.08 1.99 0 5.97 1.09 6 3.08-1.29 1.94-3.5 3.22-6 3.22z"/></svg>
            </div>
            <span>Bridal Makeup</span>
          </a>
          <a href="bridal-makeup.html#video" class="quick-icon-card">
            <div class="quick-icon-circle">
              <svg width="22" height="22" fill="currentColor" viewBox="0 0 24 24"><path d="M17 10.5V7c0-.55-.45-1-1-1H4c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1v-3.5l4 4v-11l-4 4z"/></svg>
            </div>
            <span>Bridal Video Shoot</span>
          </a>
          <a href="services.html" class="quick-icon-card">
            <div class="quick-icon-circle">
              <svg width="22" height="22" fill="currentColor" viewBox="0 0 24 24"><path d="M7 14c-1.66 0-3 1.34-3 3 0 1.31-1.16 2-2 2 .92 1.22 2.49 2 4 2 2.21 0 4-1.79 4-4 0-1.66-1.34-3-3-3zm13.71-9.37l-1.34-1.34a.996.996 0 0 0-1.41 0L9 12.25 11.75 15l8.96-8.96c.39-.39.39-1.02 0-1.41z"/></svg>
            </div>
            <span>General Makeup</span>
          </a>
          <a href="hair-body-care.html" class="quick-icon-card">
            <div class="quick-icon-circle">
              <svg width="22" height="22" fill="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/></svg>
            </div>
            <span>All Skin & Hair Care</span>
          </a>
          <a href="hair-body-care.html#body" class="quick-icon-card">
            <div class="quick-icon-circle">
              <svg width="22" height="22" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2c1.1 0 2 .9 2 2s-.9 2-2 2-2-.9-2-2 .9-2 2-2zm9 7h-6v13h-2v-6h-2v6H9V9H3V7h18v2z"/></svg>
            </div>
            <span>Body Care</span>
          </a>
          <a href="hair-body-care.html" class="quick-icon-card">
            <div class="quick-icon-circle">
              <svg width="22" height="22" fill="currentColor" viewBox="0 0 24 24"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
            </div>
            <span>Hair Care</span>
          </a>

          <!-- Row 2 -->
          <a href="special-services.html#earlobe" class="quick-icon-card">
            <div class="quick-icon-circle">
              <svg width="22" height="22" fill="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="7"/></svg>
            </div>
            <span>Ear Lobbying</span>
          </a>
          <a href="special-services.html#tattoo" class="quick-icon-card">
            <div class="quick-icon-circle">
              <svg width="22" height="22" fill="currentColor" viewBox="0 0 24 24"><polygon points="12 2 1 21 23 21"/></svg>
            </div>
            <span>Tataoo</span>
          </a>
          <a href="special-services.html#piercing" class="quick-icon-card">
            <div class="quick-icon-circle">
              <svg width="22" height="22" fill="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/></svg>
            </div>
            <span>Ear Piercing</span>
          </a>
          <a href="skin-care.html" class="quick-icon-card">
            <div class="quick-icon-circle">
              <svg width="22" height="22" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/></svg>
            </div>
            <span>Hydra Facial</span>
          </a>
          <a href="skin-care.html#laser" class="quick-icon-card">
            <div class="quick-icon-circle">
              <svg width="22" height="22" fill="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
            </div>
            <span>Carbon Laser Treatment</span>
          </a>
          <a href="special-services.html" class="quick-icon-card">
            <div class="quick-icon-circle">
              <svg width="22" height="22" fill="currentColor" viewBox="0 0 24 24"><path d="M12 3v10.55c-.59-.34-1.27-.55-2-.55-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4V7h4V3h-6z"/></svg>
            </div>
            <span>Costume Makeup (Dandiya, Party & More)</span>
          </a>
          <a href="special-services.html#mehndi" class="quick-icon-card">
            <div class="quick-icon-circle">
              <svg width="22" height="22" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm1 14h-2v-2h2zm0-4h-2V7h2z"/></svg>
            </div>
            <span>Mehandi</span>
          </a>
          <a href="skin-care.html" class="quick-icon-card">
            <div class="quick-icon-circle">
              <svg width="22" height="22" fill="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg>
            </div>
            <span>Facial & Clean Up (Many More)</span>
          </a>
        </div>
      </div>
    </div>
  </section>'''

index_html = re.sub(r'<section class="quick-icons-section">.*?</section>', quick_icons_16, index_html, flags=re.DOTALL)

# 2. Update Services section to 16 cards in .services-grid-8 matching 01-home.png
services_16 = '''<section class="section-pad bg-blush">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">OUR SERVICES</span>
        <h2>Feel the Difference with Our Premium Services</h2>
        <p>Expert care, modern hygiene standards and tailor-made beauty treatments designed to make you shine.</p>
      </div>

      <div class="services-grid-8" style="margin-bottom: 28px;">
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
      </div>

      <div class="text-center">
        <a href="services.html" class="btn btn-primary">Explore All Services &rarr;</a>
      </div>
    </div>
  </section>'''

index_html = re.sub(r'<section class="section-pad bg-blush">\s*<div class="container">\s*<div class="section-header">\s*<span class="section-tag">OUR SERVICES</span>.*?Explore All Services &rarr;</a>\s*</div>\s*</div>\s*</section>', services_16, index_html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)
print('Updated index.html successfully with 16 Quick Icons & 16 Services!')
