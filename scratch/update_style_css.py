import sys

new_css_section = '''/* ==========================================================================
   PERFECT PROPORTIONS & NATURAL CONTAINER ALIGNMENT ENGINE
   1. Clean Native 100% Zoom (NO viewport distortion or artificial left gaps)
   2. Fluid Luxury Container (24px-28px padding matching 1024px mockups)
   3. Refined Typography & Compact Proportions (0.9x scale feel natively)
   ========================================================================== */

/* 1. Refined Root Typography Scaling (Native Compact Feel) */
html {
  font-size: 14.5px !important;
  scroll-behavior: smooth;
}

@media (min-width: 1400px) {
  html {
    font-size: 15px !important;
  }
}

@media (max-width: 768px) {
  html {
    font-size: 14px !important;
  }
}

/* 2. Fluid Luxury Container (Eliminating Artificial Left Gaps) */
:root {
  --container-max: 1320px;
  --container-padding: 24px;
}

.container {
  width: 100% !important;
  max-width: var(--container-max) !important;
  margin-left: auto !important;
  margin-right: auto !important;
  padding-left: var(--container-padding) !important;
  padding-right: var(--container-padding) !important;
}

.top-bar-inner,
.header-inner {
  width: 100% !important;
  max-width: 1360px !important;
  margin-left: auto !important;
  margin-right: auto !important;
  padding-left: var(--container-padding) !important;
  padding-right: var(--container-padding) !important;
}

/* 3. Refined Section & Hero Heights */
.page-hero,
.hero-section {
  padding: 38px 0 32px !important;
}

.page-hero .hero-content h1,
.hero-content h1 {
  font-size: clamp(1.9rem, 2.8vw + 0.5rem, 2.6rem) !important;
  line-height: 1.18 !important;
  margin-bottom: 12px !important;
}

.section-padding,
.section-pad {
  padding: 42px 0 36px !important;
}

.section-pad-sm {
  padding: 26px 0 !important;
}

.section-heading h2,
.section-header h2 {
  font-size: 1.85rem !important;
  margin-bottom: 6px !important;
}

.sub-label,
.section-tag {
  font-size: 0.74rem !important;
  letter-spacing: 1.2px !important;
  padding: 3px 11px !important;
}

/* 4. Compact Card Heights & Proportional Imagery */
.service-card-img {
  height: 180px !important;
}

.product-card-img {
  height: 140px !important;
}

.ba-card .ba-image-container {
  height: 170px !important;
}

.video-thumb-card {
  height: 165px !important;
}

/* 5. Mockup-Fidelity Grids */
/* 8-column Services Grid on Desktop (Matching 01-home.png) */
.services-grid-8 {
  display: grid !important;
  grid-template-columns: repeat(8, 1fr) !important;
  gap: 12px !important;
}

@media (max-width: 1200px) {
  .services-grid-8 {
    grid-template-columns: repeat(4, 1fr) !important;
    gap: 12px !important;
  }
}

@media (max-width: 768px) {
  .services-grid-8 {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 10px !important;
  }
}

/* 16 Quick Category Circles in 8 Columns (Matching 01-home.png) */
.quick-icons-box {
  background: #ffffff;
  border: 1px solid var(--color-border);
  border-radius: 20px;
  padding: 24px 20px;
  box-shadow: 0 6px 20px rgba(0,0,0,0.03);
}

.quick-icons-grid {
  display: grid !important;
  grid-template-columns: repeat(8, 1fr) !important;
  gap: 16px !important;
}

@media (max-width: 1200px) {
  .quick-icons-grid {
    grid-template-columns: repeat(4, 1fr) !important;
    gap: 14px !important;
  }
}

@media (max-width: 600px) {
  .quick-icons-grid {
    grid-template-columns: repeat(4, 1fr) !important;
    gap: 10px !important;
  }
}

/* 6-column Featured Products Grid on Desktop (Matching 09-products.png) */
.featured-products-grid {
  display: grid !important;
  grid-template-columns: repeat(6, 1fr) !important;
  gap: 14px !important;
}

@media (max-width: 1200px) {
  .featured-products-grid {
    grid-template-columns: repeat(3, 1fr) !important;
    gap: 14px !important;
  }
}

@media (max-width: 768px) {
  .featured-products-grid {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 10px !important;
  }
}

/* 6-column Categories Grid on Desktop (Matching 09-products.png) */
.categories-grid-6 {
  display: grid !important;
  grid-template-columns: repeat(6, 1fr) !important;
  gap: 14px !important;
}

@media (max-width: 1200px) {
  .categories-grid-6 {
    grid-template-columns: repeat(3, 1fr) !important;
    gap: 14px !important;
  }
}

@media (max-width: 768px) {
  .categories-grid-6 {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 10px !important;
  }
}

/* 6-column Trust Badges Grid */
.trust-badges-grid-6 {
  display: grid !important;
  grid-template-columns: repeat(6, 1fr) !important;
  gap: 14px !important;
}

@media (max-width: 992px) {
  .trust-badges-grid-6 {
    grid-template-columns: repeat(3, 1fr) !important;
  }
}

@media (max-width: 576px) {
  .trust-badges-grid-6 {
    grid-template-columns: repeat(2, 1fr) !important;
  }
}

/* Compact Service Card */
.service-card-compact {
  background: #ffffff;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 3px 12px rgba(0,0,0,0.04);
  border: 1px solid var(--color-border);
  transition: transform 0.25s ease, box-shadow 0.25s ease;
  display: flex;
  flex-direction: column;
}

.service-card-compact:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(216, 79, 112, 0.12);
}

.service-card-compact .card-media {
  width: 100%;
  height: 105px;
  overflow: hidden;
}

.service-card-compact .card-media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.service-card-compact:hover .card-media img {
  transform: scale(1.05);
}

.service-card-compact .card-info {
  padding: 10px 8px;
  text-align: center;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.service-card-compact .card-info h4 {
  font-size: 0.84rem;
  font-weight: 600;
  color: var(--color-text-main);
  margin-bottom: 2px;
  line-height: 1.2;
}

.service-card-compact .card-info p {
  font-size: 0.70rem;
  color: var(--color-text-muted);
  line-height: 1.25;
  margin: 0;
}

.service-card-compact.special-more {
  background: linear-gradient(135deg, #fff5f7, #fdf1ea);
  border: 1.5px dashed var(--color-primary);
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 16px 10px;
  cursor: pointer;
  text-decoration: none;
}

.service-card-compact.special-more span {
  font-family: var(--font-script);
  font-size: 1.7rem;
  color: var(--color-primary);
}

/* 6. Slim Header Nav Height */
.site-header,
.main-header {
  padding: 2px 0 !important;
}

.header-inner {
  padding: 8px 0 !important;
}

.brand-logo-img {
  height: 48px !important;
}

.nav-menu .nav-link,
.nav-list .nav-link {
  padding: 6px 12px !important;
  font-size: 0.88rem !important;
}

.btn-primary,
.btn-secondary {
  padding: 10px 22px !important;
  font-size: 0.86rem !important;
}
'''

with open('css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = '/* ==========================================================================\n   NATIVE 90% LUXURY DESIGN SCALE'
start_idx = text.find(start_marker)
end_marker = '/* 7. Footer Compact Rhythm */'
end_idx = text.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_text = text[:start_idx] + new_css_section + '\n\n' + text[end_idx:]
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print('Updated css/style.css successfully!')
else:
    print(f'Markers not found! start_idx={start_idx}, end_idx={end_idx}')
