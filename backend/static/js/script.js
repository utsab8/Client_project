// Mobile Menu Toggle
const mobileMenuToggle = document.getElementById('mobileMenuToggle');
const mainNav = document.getElementById('mainNav');

// Check if we're on mobile
const isMobile = () => window.innerWidth <= 768;

if (mobileMenuToggle && mainNav) {
    // On mobile, show menu by default
    if (isMobile()) {
        mainNav.classList.add('active');
    }

    mobileMenuToggle.addEventListener('click', () => {
        if (isMobile()) {
            mainNav.classList.toggle('active');

            // Animate hamburger icon
            const spans = mobileMenuToggle.querySelectorAll('span');
            if (mainNav.classList.contains('active')) {
                spans[0].style.transform = 'rotate(45deg) translateY(10px)';
                spans[1].style.opacity = '0';
                spans[2].style.transform = 'rotate(-45deg) translateY(-10px)';
            } else {
                spans[0].style.transform = 'none';
                spans[1].style.opacity = '1';
                spans[2].style.transform = 'none';
            }
        }
    });

    // Update on window resize
    window.addEventListener('resize', () => {
        if (isMobile()) {
            mainNav.classList.add('active');
        } else {
            mainNav.classList.remove('active');
            const spans = mobileMenuToggle.querySelectorAll('span');
            spans[0].style.transform = 'none';
            spans[1].style.opacity = '1';
            spans[2].style.transform = 'none';
        }
    });
}

// Mobile Follow Us dropdown toggle
document.addEventListener('DOMContentLoaded', () => {
    const navFollow = document.querySelector('.nav-follow');
    const navFollowLink = navFollow?.querySelector('a');
    
    // Check if we're on mobile (screen width <= 768px)
    const isMobile = () => window.innerWidth <= 768;
    
    if (navFollowLink) {
        navFollowLink.addEventListener('click', (e) => {
            if (isMobile()) {
                e.preventDefault();
                const menu = navFollow.querySelector('.nav-follow-menu');
                if (menu) {
                    menu.classList.toggle('active');
                }
            }
        });
    }
    
    // Close dropdown when clicking outside on mobile
    document.addEventListener('click', (e) => {
        if (isMobile() && navFollow && !navFollow.contains(e.target)) {
            const menu = navFollow.querySelector('.nav-follow-menu');
            if (menu) {
                menu.classList.remove('active');
            }
        }
    });

    // Enhanced horizontal scrolling for mobile menu
    const navList = document.querySelector('.nav-list');
    if (navList && isMobile()) {
        let isDown = false;
        let startX;
        let scrollLeft;

        navList.addEventListener('mousedown', (e) => {
            isDown = true;
            navList.style.cursor = 'grabbing';
            startX = e.pageX - navList.offsetLeft;
            scrollLeft = navList.scrollLeft;
        });

        navList.addEventListener('mouseleave', () => {
            isDown = false;
            navList.style.cursor = 'grab';
        });

        navList.addEventListener('mouseup', () => {
            isDown = false;
            navList.style.cursor = 'grab';
        });

        navList.addEventListener('mousemove', (e) => {
            if (!isDown) return;
            e.preventDefault();
            const x = e.pageX - navList.offsetLeft;
            const walk = (x - startX) * 2;
            navList.scrollLeft = scrollLeft - walk;
        });

        // Touch support for mobile
        let touchStartX = 0;
        let touchScrollLeft = 0;

        navList.addEventListener('touchstart', (e) => {
            touchStartX = e.touches[0].pageX - navList.offsetLeft;
            touchScrollLeft = navList.scrollLeft;
        });

        navList.addEventListener('touchmove', (e) => {
            if (!e.touches.length) return;
            const x = e.touches[0].pageX - navList.offsetLeft;
            const walk = (x - touchStartX) * 1.5;
            navList.scrollLeft = touchScrollLeft - walk;
        });

        // Set cursor style
        navList.style.cursor = 'grab';
    }
});

// Smooth Scrolling for Anchor Links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href !== '#' && href !== '') {
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });

                // Close mobile menu if open
                if (mainNav && mainNav.classList.contains('active')) {
                    mainNav.classList.remove('active');
                    const spans = mobileMenuToggle.querySelectorAll('span');
                    spans[0].style.transform = 'none';
                    spans[1].style.opacity = '1';
                    spans[2].style.transform = 'none';
                }
            }
        }
    });
});

// Scroll Animation for Elements
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe all product cards and category cards
document.addEventListener('DOMContentLoaded', () => {
    const animatedElements = document.querySelectorAll('.product-card, .category-card');

    animatedElements.forEach((el, index) => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = `all 0.6s ease-out ${index * 0.1}s`;
        observer.observe(el);
    });
});

// Product Card Click Handler removed to allow HTML href navigation
// Buy Button Handler removed as buttons are now direct links

// Add ripple animation to CSS dynamically
const style = document.createElement('style');
style.textContent = `
    @keyframes ripple {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Header Scroll Effect
let lastScroll = 0;
const header = document.querySelector('.header');

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;

    if (currentScroll <= 0) {
        header.style.boxShadow = '0 10px 15px -3px rgba(0, 0, 0, 0.1)';
    } else {
        header.style.boxShadow = '0 20px 25px -5px rgba(0, 0, 0, 0.3)';
    }

    // Hide/show header on scroll
    if (currentScroll > lastScroll && currentScroll > 100) {
        header.style.transform = 'translateY(-100%)';
    } else {
        header.style.transform = 'translateY(0)';
    }

    lastScroll = currentScroll;
});

// Add transition to header
header.style.transition = 'transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out';

// Load More Button - Show remaining products
const loadMoreBtn = document.getElementById('loadMoreBtn');
const loadMoreContainer = document.getElementById('loadMoreContainer');

if (loadMoreBtn) {
    loadMoreBtn.addEventListener('click', () => {
        // Get all hidden products (those with product-hidden class and display:none)
        const allHiddenProducts = document.querySelectorAll('.product-card.product-hidden');
        const hiddenProducts = Array.from(allHiddenProducts).filter(product => {
            // Only include products that are hidden by our logic, not by price filtering
            // If it has display:none but is part of the filtered set, include it
            return true;
        });
        
        if (hiddenProducts.length === 0) {
            // No more products to show
            if (loadMoreContainer) {
                loadMoreContainer.style.display = 'none';
            }
            return;
        }

        // Add loading animation
        const originalText = loadMoreBtn.textContent;
        loadMoreBtn.textContent = 'Loading...';
        loadMoreBtn.style.opacity = '0.7';
        loadMoreBtn.style.cursor = 'not-allowed';
        loadMoreBtn.disabled = true;

        // Show hidden products with animation
        setTimeout(() => {
            hiddenProducts.forEach((product, index) => {
                setTimeout(() => {
                    product.classList.remove('product-hidden');
                    product.style.display = ''; // Reset display to show the product
                    product.style.opacity = '0';
                    product.style.transform = 'translateY(20px)';
                    product.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
                    
                    // Trigger reflow
                    product.offsetHeight;
                    
                    // Animate in
                    product.style.opacity = '1';
                    product.style.transform = 'translateY(0)';
                }, index * 50); // Stagger animation
            });

            // Check if there are more products to show
            setTimeout(() => {
                const remainingHidden = document.querySelectorAll('.product-card.product-hidden');
                if (remainingHidden.length === 0) {
                    // Hide load more button if all products are shown
                    if (loadMoreContainer) {
                        loadMoreContainer.style.display = 'none';
                    }
                } else {
                    // Reset button
                    loadMoreBtn.textContent = originalText;
                    loadMoreBtn.style.opacity = '1';
                    loadMoreBtn.style.cursor = 'pointer';
                    loadMoreBtn.disabled = false;
                }
            }, hiddenProducts.length * 50 + 300);
        }, 300);
    });
}

// Add hover effect to product images
document.querySelectorAll('.product-image').forEach(img => {
    img.addEventListener('mouseenter', function () {
        this.style.transform = 'scale(1.05)';
        this.style.transition = 'transform 0.3s ease-out';
    });

    img.addEventListener('mouseleave', function () {
        this.style.transform = 'scale(1)';
    });
});

// Parallax effect for hero section
window.addEventListener('scroll', () => {
    const hero = document.querySelector('.hero');
    if (hero) {
        const scrolled = window.pageYOffset;
        const parallax = scrolled * 0.5;
        hero.style.transform = `translateY(${parallax}px)`;
    }
});

// Add active state to navigation based on scroll position
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-list a[href^="#"]');

window.addEventListener('scroll', () => {
    let current = '';

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (pageYOffset >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
});

// Add typing effect to hero title (optional enhancement)
function typeWriter(element, text, speed = 100) {
    let i = 0;
    element.textContent = '';

    function type() {
        if (i < text.length) {
            element.textContent += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    }

    type();
}

// Uncomment to enable typing effect on page load
// window.addEventListener('load', () => {
//     const heroTitle = document.querySelector('.hero-title');
//     if (heroTitle) {
//         const originalText = heroTitle.textContent;
//         typeWriter(heroTitle, originalText, 50);
//     }
// });

// Checkout form handling (single-page)
const checkoutForm = document.getElementById('checkoutForm');
if (checkoutForm) {
    checkoutForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const email = document.getElementById('email')?.value;
        const phone = document.getElementById('phone')?.value;
        if (email && phone) {
            alert('Thank you for your purchase! You will receive the download link via email shortly.');
        }
    });
}

// Console welcome message
console.log('%c🚀 Welcome to Skilcart (single-page version)! ', 'background: linear-gradient(135deg, #6366f1, #ec4899); color: white; font-size: 20px; padding: 10px; border-radius: 5px;');
console.log('%cWebsite cloned, consolidated into one HTML, and optimized for simple checkout.', 'color: #10b981; font-size: 14px;');

// Price Filtering Logic
document.addEventListener('DOMContentLoaded', () => {
    const urlParams = new URLSearchParams(window.location.search);
    const filterPrice = urlParams.get('price');

    if (filterPrice) {
        const productCards = document.querySelectorAll('.product-card[data-price]');
        let visibleCount = 0;
        const matchingProducts = [];

        // First, collect all matching products
        productCards.forEach(card => {
            const price = card.getAttribute('data-price');
            if (price === filterPrice) {
                matchingProducts.push(card);
            } else {
                // Hide cards that don't match the price filter completely
                card.style.display = 'none';
                card.classList.add('product-hidden');
            }
        });

        // Show first 9 matching products, hide the rest
        matchingProducts.forEach((card, index) => {
            if (index < 9) {
                card.style.display = '';
                card.classList.remove('product-hidden');
                visibleCount++;
            } else {
                card.style.display = 'none';
                card.classList.add('product-hidden');
            }
        });

        // Show/hide load more button based on filtered results
        const hiddenFilteredProducts = matchingProducts.filter((card, index) => index >= 9);
        const loadMoreContainer = document.getElementById('loadMoreContainer');
        if (hiddenFilteredProducts.length > 0 && loadMoreContainer) {
            loadMoreContainer.style.display = 'block';
        } else if (loadMoreContainer) {
            loadMoreContainer.style.display = 'none';
        }

        // Scroll to products if filtered
        if (matchingProducts.length > 0) {
            const productsSection = document.querySelector('.product-grid') || document.querySelector('#reels-bundle');
            if (productsSection) {
                // Small delay to ensure layout matches
                setTimeout(() => {
                    productsSection.scrollIntoView({ behavior: 'smooth' });
                }, 100);
            }
        }
    } else {
        // No price filter - ensure load more works with default 9 products
        const hiddenProducts = document.querySelectorAll('.product-card.product-hidden');
        const loadMoreContainer = document.getElementById('loadMoreContainer');
        if (hiddenProducts.length > 0 && loadMoreContainer) {
            loadMoreContainer.style.display = 'block';
        } else if (loadMoreContainer) {
            loadMoreContainer.style.display = 'none';
        }
    }
});
