/**
 * Neelam Beauty Studio (Hello Aesthetic by - NBS)
 * Master Production JavaScript Engine
 * Complete interactive features:
 * - Mobile drawer navigation & backdrop blur
 * - FAQ accordions
 * - Gallery & Special Services & Blog category filters
 * - Blog live instant search
 * - Interactive 3-step appointment wizard with validation & WhatsApp dispatch
 * - Auto-service pre-selection from URL parameter
 * - Academy & Products horizontal carousel controls
 * - Video showcase playback modal
 * - Gallery full-resolution image lightbox
 * - Contact form interactive submission & confirmation modal
 * - Newsletter subscription toast feedback
 */

document.addEventListener('DOMContentLoaded', () => {
  initMobileDrawer();
  initFaqAccordions();
  initGalleryAndBlogFilters();
  initBlogSearch();
  initAppointmentStepper();
  initCarousels();
  initVideoModals();
  initImageLightbox();
  initContactForm();
  initNewsletters();
});

/* --- 1. Mobile Navigation Drawer & Touch Experience --- */
function initMobileDrawer() {
  const toggleBtn = document.querySelector('.mobile-nav-toggle');
  const drawer = document.querySelector('.mobile-nav-drawer');
  const closeBtn = document.querySelector('.mobile-nav-close');

  let overlay = document.querySelector('.mobile-nav-overlay');
  if (!overlay && drawer) {
    overlay = document.createElement('div');
    overlay.className = 'mobile-nav-overlay';
    document.body.appendChild(overlay);
  }

  function openDrawer() {
    if (drawer) drawer.classList.add('open');
    if (overlay) overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    if (drawer) drawer.classList.remove('open');
    if (overlay) overlay.classList.remove('open');
    document.body.style.overflow = '';
  }

  if (toggleBtn) {
    toggleBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      openDrawer();
    });
  }

  if (closeBtn) {
    closeBtn.addEventListener('click', closeDrawer);
  }

  if (overlay) {
    overlay.addEventListener('click', closeDrawer);
  }

  if (drawer) {
    const navLinks = drawer.querySelectorAll('a');
    navLinks.forEach(link => {
      link.addEventListener('click', closeDrawer);
    });
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && drawer && drawer.classList.contains('open')) {
      closeDrawer();
    }
  });
}

/* --- 2. FAQ Accordions --- */
function initFaqAccordions() {
  const faqItems = document.querySelectorAll('.faq-item, .accordion-item');

  faqItems.forEach(item => {
    const questionBtn = item.querySelector('.faq-question, .accordion-header');
    if (questionBtn) {
      questionBtn.addEventListener('click', () => {
        const isOpen = item.classList.contains('active');

        // Close other open accordions in the same list
        faqItems.forEach(other => {
          if (other !== item) other.classList.remove('active');
        });

        // Toggle current item
        if (!isOpen) {
          item.classList.add('active');
        } else {
          item.classList.remove('active');
        }
      });
    }
  });
}

/* --- 3. Gallery & Blog Category Filters --- */
function initGalleryAndBlogFilters() {
  const filterBtns = document.querySelectorAll('.gallery-filter-btn, .filter-tab-btn');
  const filterableItems = document.querySelectorAll('.gallery-item-card, .blog-card, [data-category]');

  if (filterBtns.length > 0 && filterableItems.length > 0) {
    filterBtns.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();

        // Scope to closest container
        const parentNav = btn.closest('.gallery-filter-nav') || btn.parentElement;
        if (parentNav) {
          parentNav.querySelectorAll('.gallery-filter-btn, .filter-tab-btn').forEach(b => b.classList.remove('active'));
        }
        btn.classList.add('active');

        const filter = (btn.getAttribute('data-filter') || 'all').toLowerCase().trim();

        // Target relevant cards inside the same section or page
        const section = btn.closest('section') || document;
        const targetCards = section.querySelectorAll('.gallery-item-card, .blog-card, [data-category]');

        targetCards.forEach(card => {
          const cat = (card.getAttribute('data-category') || '').toLowerCase().trim();
          if (filter === 'all' || cat.includes(filter) || filter.includes(cat)) {
            card.style.display = '';
            card.style.opacity = '1';
            card.style.transform = 'scale(1)';
          } else {
            card.style.display = 'none';
            card.style.opacity = '0';
          }
        });
      });
    });
  }

  // Load More Gallery Button
  const loadMoreBtn = document.getElementById('loadMoreGalleryBtn');
  if (loadMoreBtn) {
    loadMoreBtn.addEventListener('click', () => {
      loadMoreBtn.textContent = 'All Photos Loaded';
      loadMoreBtn.disabled = true;
      loadMoreBtn.style.opacity = '0.7';
    });
  }
}

/* --- 4. Blog Live Instant Search --- */
function initBlogSearch() {
  const searchInput = document.getElementById('blogSearchInput');
  const blogCards = document.querySelectorAll('.blog-card');

  if (searchInput && blogCards.length > 0) {
    searchInput.addEventListener('input', (e) => {
      const query = e.target.value.toLowerCase().trim();

      blogCards.forEach(card => {
        const title = (card.querySelector('h3')?.textContent || '').toLowerCase();
        const excerpt = (card.querySelector('p')?.textContent || '').toLowerCase();
        const badge = (card.querySelector('.blog-badge-tag')?.textContent || '').toLowerCase();

        if (!query || title.includes(query) || excerpt.includes(query) || badge.includes(query)) {
          card.style.display = '';
          card.style.opacity = '1';
        } else {
          card.style.display = 'none';
          card.style.opacity = '0';
        }
      });
    });
  }
}

/* --- 5. Interactive 3-Step Appointment Stepper & Auto-Select --- */
function initAppointmentStepper() {
  const clientName = document.getElementById('clientName') || document.getElementById('bookName');
  const clientPhone = document.getElementById('clientPhone') || document.getElementById('bookPhone');
  const clientService = document.getElementById('clientService') || document.getElementById('bookService');
  const clientDate = document.getElementById('clientDate') || document.getElementById('bookDate');
  const clientTime = document.getElementById('clientTime') || document.getElementById('bookTime');
  const clientNotes = document.getElementById('clientNotes');

  // Summary targets
  const sumService = document.getElementById('sumService');
  const sumDate = document.getElementById('sumDate');
  const sumTime = document.getElementById('sumTime');
  const sumName = document.getElementById('sumName');
  const sumPhone = document.getElementById('sumPhone') || document.getElementById('sumMobile');

  // Review step targets
  const revName = document.getElementById('revName');
  const revPhone = document.getElementById('revPhone');
  const revService = document.getElementById('revService');
  const revDateTime = document.getElementById('revDateTime');
  const revNotes = document.getElementById('revNotes');

  // Stepper UI
  const stepNode1 = document.getElementById('stepNode1');
  const stepNode2 = document.getElementById('stepNode2');
  const stepNode3 = document.getElementById('stepNode3');

  const step1 = document.getElementById('bookingStep1') || document.getElementById('step1Content');
  const step2 = document.getElementById('bookingStep2') || document.getElementById('step2Content');
  const step3 = document.getElementById('bookingStep3') || document.getElementById('step3Content');

  const btnNext = document.getElementById('btnNextStep') || document.getElementById('nextStepBtn');
  const btnPrev = document.getElementById('btnPrevStep');
  const btnConfirm = document.getElementById('btnConfirmBooking');

  // Check URL parameters for pre-selected service (e.g. ?service=Bridal+Makeup)
  const urlParams = new URLSearchParams(window.location.search);
  const serviceParam = urlParams.get('service');
  if (serviceParam && clientService) {
    for (let opt of clientService.options) {
      if (opt.text.toLowerCase().includes(serviceParam.toLowerCase()) || opt.value.toLowerCase().includes(serviceParam.toLowerCase())) {
        clientService.value = opt.value;
        break;
      }
    }
  }

  function syncSummary() {
    if (sumService && clientService) sumService.textContent = clientService.value || 'Not Selected';
    if (sumDate && clientDate) sumDate.textContent = clientDate.value || 'Not Selected';
    if (sumTime && clientTime) sumTime.textContent = clientTime.value || 'Not Selected';
    if (sumName && clientName) sumName.textContent = clientName.value.trim() || 'Not Added';
    if (sumPhone && clientPhone) sumPhone.textContent = clientPhone.value.trim() || 'Not Added';
  }

  // Initial sync
  syncSummary();

  [clientName, clientPhone, clientService, clientDate, clientTime, clientNotes].forEach(input => {
    if (input) {
      input.addEventListener('input', syncSummary);
      input.addEventListener('change', syncSummary);
    }
  });

  // Step 1 -> Step 2
  if (btnNext) {
    btnNext.addEventListener('click', () => {
      if (!clientName || !clientName.value.trim()) {
        alert('Please enter your Full Name.');
        clientName?.focus();
        return;
      }
      if (!clientPhone || !clientPhone.value.trim()) {
        alert('Please enter your Mobile Number.');
        clientPhone?.focus();
        return;
      }
      if (!clientService || !clientService.value) {
        alert('Please select a Service.');
        clientService?.focus();
        return;
      }
      if (!clientDate || !clientDate.value) {
        alert('Please select your Preferred Date.');
        clientDate?.focus();
        return;
      }
      if (!clientTime || !clientTime.value) {
        alert('Please select your Preferred Time.');
        clientTime?.focus();
        return;
      }

      // Populate Step 2 Review
      if (revName) revName.textContent = clientName.value;
      if (revPhone) revPhone.textContent = clientPhone.value;
      if (revService) revService.textContent = clientService.value;
      if (revDateTime) revDateTime.textContent = `${clientDate.value} at ${clientTime.value}`;
      if (revNotes) revNotes.textContent = clientNotes?.value.trim() || 'No special notes';

      // Switch to Step 2
      if (step1) step1.style.display = 'none';
      if (step2) step2.style.display = 'block';
      if (stepNode1) stepNode1.classList.remove('active');
      if (stepNode2) stepNode2.classList.add('active');

      window.scrollTo({ top: (step2?.offsetTop || 200) - 100, behavior: 'smooth' });
    });
  }

  // Step 2 -> Step 1 (Back)
  if (btnPrev) {
    btnPrev.addEventListener('click', () => {
      if (step2) step2.style.display = 'none';
      if (step1) step1.style.display = 'block';
      if (stepNode2) stepNode2.classList.remove('active');
      if (stepNode1) stepNode1.classList.add('active');
    });
  }

  // Step 2 -> Step 3 (Confirm & WhatsApp)
  if (btnConfirm) {
    btnConfirm.addEventListener('click', () => {
      const name = clientName?.value || '';
      const phone = clientPhone?.value || '';
      const service = clientService?.value || '';
      const date = clientDate?.value || '';
      const time = clientTime?.value || '';
      const notes = clientNotes?.value || '';

      const waMsg = `Hello Neelam Beauty Studio! I would like to book an appointment:\n\n*Name:* ${name}\n*Phone:* ${phone}\n*Service:* ${service}\n*Date:* ${date}\n*Time:* ${time}\n*Notes:* ${notes || 'None'}\n\nPlease confirm my slot. Thank you!`;
      const waUrl = `https://wa.me/919000000000?text=${encodeURIComponent(waMsg)}`;

      // Switch to Step 3
      if (step2) step2.style.display = 'none';
      if (step3) step3.style.display = 'block';
      if (stepNode2) stepNode2.classList.remove('active');
      if (stepNode3) stepNode3.classList.add('active');

      // Open WhatsApp in new tab
      window.open(waUrl, '_blank');
    });
  }
}

/* --- 6. Carousel Smooth Navigation Controls --- */
function initCarousels() {
  document.querySelectorAll('.carousel-container-relative').forEach(carousel => {
    const prevBtn = carousel.querySelector('.carousel-nav-btn.prev-btn, .carousel-nav-btn.prev');
    const nextBtn = carousel.querySelector('.carousel-nav-btn.next-btn, .carousel-nav-btn.next');
    const track = carousel.querySelector('.gallery-masonry-grid, .testimonials-grid, .best-sellers-strip, .cards-grid-6');

    if (track) {
      track.style.overflowX = 'auto';
      track.style.scrollBehavior = 'smooth';

      if (prevBtn) {
        prevBtn.addEventListener('click', (e) => {
          e.preventDefault();
          const scrollAmt = track.clientWidth * 0.75;
          track.scrollBy({ left: -scrollAmt, behavior: 'smooth' });
        });
      }

      if (nextBtn) {
        nextBtn.addEventListener('click', (e) => {
          e.preventDefault();
          const scrollAmt = track.clientWidth * 0.75;
          track.scrollBy({ left: scrollAmt, behavior: 'smooth' });
        });
      }
    }
  });
}

/* --- 7. Video Showcase Modal --- */
function initVideoModals() {
  const videoCards = document.querySelectorAll('.video-thumb-card');
  if (videoCards.length === 0) return;

  // Create video modal container if not present
  let modal = document.getElementById('videoPlayerModal');
  if (!modal) {
    modal = document.createElement('div');
    modal.id = 'videoPlayerModal';
    modal.className = 'luxury-video-modal';
    modal.innerHTML = `
      <div class="video-modal-backdrop"></div>
      <div class="video-modal-dialog">
        <button class="video-modal-close" aria-label="Close video">&times;</button>
        <div class="video-modal-header">
          <span class="video-modal-badge">NEELAM BEAUTY STUDIO REELS</span>
          <h3 id="videoModalTitle">Video Showcase</h3>
        </div>
        <div class="video-player-frame">
          <div class="video-mock-playing">
            <svg width="64" height="64" viewBox="0 0 24 24" fill="var(--color-accent-rose)"><polygon points="5 3 19 12 5 21 5 3"/></svg>
            <p>Playing Studio Showcase Reel...</p>
            <div class="sound-wave">
              <span></span><span></span><span></span><span></span><span></span>
            </div>
          </div>
        </div>
        <div class="video-modal-footer">
          <a href="appointment.html" class="btn btn-primary btn-sm">Book This Makeover &rarr;</a>
        </div>
      </div>
    `;
    document.body.appendChild(modal);
  }

  const titleEl = modal.querySelector('#videoModalTitle');
  const closeBtn = modal.querySelector('.video-modal-close');
  const backdrop = modal.querySelector('.video-modal-backdrop');

  function openVideoModal(title) {
    if (titleEl) titleEl.textContent = title || 'Studio Transformation Reel';
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeVideoModal() {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }

  videoCards.forEach(card => {
    card.addEventListener('click', () => {
      const title = card.querySelector('.video-card-title')?.textContent || card.querySelector('img')?.alt || 'Beauty Reel';
      openVideoModal(title);
    });
  });

  if (closeBtn) closeBtn.addEventListener('click', closeVideoModal);
  if (backdrop) backdrop.addEventListener('click', closeVideoModal);

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('active')) {
      closeVideoModal();
    }
  });
}

/* --- 8. Gallery High-Resolution Image Lightbox --- */
function initImageLightbox() {
  const galleryItems = document.querySelectorAll('.gallery-masonry-grid .gallery-item-card, .cards-grid-5 .ba-card');
  if (galleryItems.length === 0) return;

  let lightbox = document.getElementById('imageLightboxModal');
  if (!lightbox) {
    lightbox = document.createElement('div');
    lightbox.id = 'imageLightboxModal';
    lightbox.className = 'luxury-lightbox-modal';
    lightbox.innerHTML = `
      <div class="lightbox-backdrop"></div>
      <div class="lightbox-content">
        <button class="lightbox-close" aria-label="Close image">&times;</button>
        <img id="lightboxImg" src="" alt="Gallery Image Preview">
        <div id="lightboxCaption" class="lightbox-caption"></div>
      </div>
    `;
    document.body.appendChild(lightbox);
  }

  const imgEl = lightbox.querySelector('#lightboxImg');
  const capEl = lightbox.querySelector('#lightboxCaption');
  const closeBtn = lightbox.querySelector('.lightbox-close');
  const backdrop = lightbox.querySelector('.lightbox-backdrop');

  function openLightbox(src, caption) {
    if (imgEl) imgEl.src = src;
    if (capEl) capEl.textContent = caption || 'Neelam Beauty Studio';
    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    lightbox.classList.remove('active');
    document.body.style.overflow = '';
  }

  galleryItems.forEach(item => {
    item.style.cursor = 'pointer';
    item.addEventListener('click', () => {
      const img = item.querySelector('img');
      const caption = item.querySelector('.gallery-overlay-hover span, h4, p')?.textContent || img?.alt || 'Portfolio Photograph';
      if (img && img.src) {
        openLightbox(img.src, caption);
      }
    });
  });

  if (closeBtn) closeBtn.addEventListener('click', closeLightbox);
  if (backdrop) backdrop.addEventListener('click', closeLightbox);

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && lightbox.classList.contains('active')) {
      closeLightbox();
    }
  });
}

/* --- 9. Interactive Contact Form Submission --- */
function initContactForm() {
  const contactForms = document.querySelectorAll('form[action="appointment.html"], form#contactForm');

  contactForms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();

      const nameInput = form.querySelector('input[type="text"]');
      const phoneInput = form.querySelector('input[type="tel"]');
      const serviceInput = form.querySelector('select');
      const msgInput = form.querySelector('textarea');

      const name = nameInput?.value.trim() || 'Valued Client';
      const phone = phoneInput?.value.trim() || 'Not Provided';
      const service = serviceInput?.value || 'General Inquiry';
      const msg = msgInput?.value.trim() || 'I would like to enquire about your services.';

      // Construct WhatsApp message
      const waText = `Hello Neelam Beauty Studio! I submitted an enquiry:\n\n*Name:* ${name}\n*Phone:* ${phone}\n*Service:* ${service}\n*Message:* ${msg}`;
      const waUrl = `https://wa.me/919000000000?text=${encodeURIComponent(waText)}`;

      // Show beautiful success modal
      let confirmModal = document.getElementById('contactSuccessModal');
      if (!confirmModal) {
        confirmModal = document.createElement('div');
        confirmModal.id = 'contactSuccessModal';
        confirmModal.className = 'luxury-video-modal';
        document.body.appendChild(confirmModal);
      }

      confirmModal.innerHTML = `
        <div class="video-modal-backdrop"></div>
        <div class="video-modal-dialog" style="max-width: 480px; text-align: center; padding: 35px 25px;">
          <button class="video-modal-close" onclick="this.closest('#contactSuccessModal').classList.remove('active'); document.body.style.overflow='';" aria-label="Close">&times;</button>
          <div style="width: 60px; height: 60px; border-radius: 50%; background: #e8f8f0; color: #25d366; display: flex; align-items: center; justify-content: center; margin: 0 auto 16px auto;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          </div>
          <h3 style="font-size: 1.4rem; color: var(--color-text-dark); margin-bottom: 8px;">Enquiry Sent Successfully!</h3>
          <p style="font-size: 0.9rem; color: var(--color-text-muted); line-height: 1.6; margin-bottom: 22px;">
            Thank you, <strong>${name}</strong>! Our studio team has received your message and will contact you shortly on <strong>${phone}</strong>.
          </p>
          <div style="display: flex; flex-direction: column; gap: 10px;">
            <a href="${waUrl}" target="_blank" class="btn btn-primary" style="background: #25d366; border-color: #25d366; display: flex; align-items: center; justify-content: center; gap: 8px;">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z"/></svg>
              Chat on WhatsApp Directly
            </a>
            <button class="btn btn-secondary" onclick="this.closest('#contactSuccessModal').classList.remove('active'); document.body.style.overflow='';">
              Close Window
            </button>
          </div>
        </div>
      `;

      confirmModal.classList.add('active');
      document.body.style.overflow = 'hidden';
      form.reset();
    });
  });
}

/* --- 10. Newsletter Subscriptions --- */
function initNewsletters() {
  const newsletterForms = document.querySelectorAll('.newsletter-box-inner, .stay-updated-form, form[action*="newsletter"]');

  newsletterForms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const emailInput = form.querySelector('input[type="email"]');
      if (emailInput && emailInput.value.trim()) {
        const userEmail = emailInput.value.trim();
        emailInput.value = '';
        alert(`Thank you for subscribing! Exclusive beauty tips and studio offers will be sent to: ${userEmail}`);
      }
    });
  });
}
