/**
 * Skillcart API Client
 * Handles all API interactions with the Django REST Framework backend
 */

const API_BASE_URL = 'http://localhost:8000/api';

class SkillcartAPI {
    constructor(baseURL = API_BASE_URL) {
        this.baseURL = baseURL;
    }

    /**
     * Generic fetch method with error handling
     */
    async fetch(endpoint, options = {}) {
        try {
            const response = await fetch(`${this.baseURL}${endpoint}`, {
                headers: {
                    'Content-Type': 'application/json',
                    ...options.headers,
                },
                ...options,
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            return await response.json();
        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    }

    /**
     * Get all products
     */
    async getProducts(params = {}) {
        const queryString = new URLSearchParams(params).toString();
        const endpoint = `/products/${queryString ? `?${queryString}` : ''}`;
        return this.fetch(endpoint);
    }

    /**
     * Get product by ID
     */
    async getProduct(id) {
        return this.fetch(`/products/${id}/`);
    }

    /**
     * Get product by slug
     */
    async getProductBySlug(slug) {
        const products = await this.getProducts({ search: slug });
        return products.results?.find(p => p.slug === slug) || products.find(p => p.slug === slug);
    }

    /**
     * Get featured products
     */
    async getFeaturedProducts() {
        return this.fetch('/products/featured/');
    }

    /**
     * Get products by price range
     */
    async getProductsByPrice(minPrice, maxPrice) {
        const params = {};
        if (minPrice) params.min_price = minPrice;
        if (maxPrice) params.max_price = maxPrice;
        return this.fetch(`/products/by_price/?${new URLSearchParams(params).toString()}`);
    }

    /**
     * Get products by category
     */
    async getProductsByCategory(categorySlug) {
        return this.fetch(`/products/by_category/?category=${categorySlug}`);
    }

    /**
     * Get all categories
     */
    async getCategories() {
        return this.fetch('/categories/');
    }

    /**
     * Get category by slug
     */
    async getCategory(slug) {
        return this.fetch(`/categories/${slug}/`);
    }

    /**
     * Get all tags
     */
    async getTags() {
        return this.fetch('/tags/');
    }

    /**
     * Create an order
     */
    async createOrder(orderData) {
        return this.fetch('/orders/', {
            method: 'POST',
            body: JSON.stringify(orderData),
        });
    }

    /**
     * Get order by ID
     */
    async getOrder(orderId) {
        return this.fetch(`/orders/${orderId}/`);
    }

    /**
     * Get orders by email
     */
    async getOrdersByEmail(email) {
        return this.fetch(`/orders/by_email/?email=${encodeURIComponent(email)}`);
    }

    /**
     * Update order status
     */
    async updateOrderStatus(orderId, statusData) {
        return this.fetch(`/orders/${orderId}/update_status/`, {
            method: 'PATCH',
            body: JSON.stringify(statusData),
        });
    }

    /**
     * Get site settings
     */
    async getSettings() {
        const result = await this.fetch('/settings/');
        return Array.isArray(result) ? result[0] : result;
    }
}

// Create global instance
const api = new SkillcartAPI();

// Export for use in modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { SkillcartAPI, api };
}

/**
 * Frontend Helper Functions
 */

/**
 * Render products to the page
 */
async function renderProducts(containerSelector, filters = {}) {
    const container = document.querySelector(containerSelector);
    if (!container) {
        console.error(`Container ${containerSelector} not found`);
        return;
    }

    try {
        const data = await api.getProducts(filters);
        const products = data.results || data;

        if (products.length === 0) {
            container.innerHTML = '<p>No products found.</p>';
            return;
        }

        // Loop through all products from API - automatically shows any product added via admin
        container.innerHTML = products.map(product => `
            <a href="product.html?slug=${product.slug}" class="product-card" data-product="${product.slug}" data-price="${product.price}" style="text-decoration: none; color: inherit;">
                <div class="product-image" style="background: linear-gradient(135deg, #00a651, #003a12);">
                    ${product.badge_text ? `<div class="product-badge">${product.badge_text}</div>` : ''}
                </div>
                <div class="product-content">
                    <h3 class="product-title">${product.name}</h3>
                    <div class="product-price-row">
                        <span class="price-amount">₹${product.price}</span>
                        ${product.discount_percentage > 0 ? `<span class="discount-badge"><i class="fa-solid fa-tag"></i> ${product.discount_percentage}% Off</span>` : ''}
                    </div>
                </div>
            </a>
        `).join('');

        // Re-initialize animations if needed
        initializeProductAnimations();
    } catch (error) {
        console.error('Error loading products:', error);
        container.innerHTML = '<p>Error loading products. Please try again later.</p>';
    }
}

/**
 * Render product details
 */
async function renderProductDetails(slug) {
    try {
        // Try to get product by slug from API
        const products = await api.getProducts({ search: slug });
        const productList = products.results || products;
        const product = productList.find(p => p.slug === slug);
        
        if (!product) {
            console.error('Product not found:', slug);
            // Show error message
            const mainContent = document.querySelector('.product-main');
            if (mainContent) {
                mainContent.innerHTML = `
                    <div style="text-align: center; padding: 3rem;">
                        <h2>Product Not Found</h2>
                        <p>The product you're looking for doesn't exist.</p>
                        <a href="../index.html" style="color: #003a12; text-decoration: underline;">Go back to homepage</a>
                    </div>
                `;
            }
            return;
        }

        // Get full product details
        const fullProduct = await api.getProduct(product.id);

        // Update page title and meta
        document.title = `${fullProduct.name} - Skilcart`;
        const metaDesc = document.querySelector('meta[name="description"]');
        if (metaDesc) {
            metaDesc.content = fullProduct.short_description || fullProduct.description.substring(0, 160);
        }

        // Update breadcrumb
        const breadcrumb = document.querySelector('.breadcrumb span') || document.getElementById('breadcrumbProductName');
        if (breadcrumb) breadcrumb.textContent = fullProduct.name;

        // Update product title
        const titleEl = document.querySelector('.product-page-title');
        if (titleEl) titleEl.textContent = fullProduct.name;

        // Update product image
        const imageEl = document.querySelector('.product-featured-image');
        if (imageEl) {
            if (fullProduct.display_image) {
                imageEl.innerHTML = `<img src="${fullProduct.display_image}" alt="${fullProduct.name}" style="width: 100%; height: auto; border-radius: 8px;">`;
            } else {
                imageEl.innerHTML = `
                    <div class="product-banner-placeholder" style="background: linear-gradient(135deg, #1dbf73, #003a12); color: white; display: flex; align-items: center; justify-content: center; height: 400px; font-size: 2rem; font-weight: 700; border-radius: 8px;">
                        ${fullProduct.name}
                    </div>
                `;
            }
        }

        // Update price
        const priceEl = document.querySelector('.product-price');
        if (priceEl) priceEl.textContent = `₹${fullProduct.price}`;

        // Update discount
        const discountEl = document.querySelector('.product-discount');
        if (discountEl && fullProduct.discount_percentage > 0) {
            discountEl.textContent = `${fullProduct.discount_percentage}% OFF`;
        }

        // Update description
        const descEl = document.querySelector('.product-description');
        if (descEl) {
            let html = `<h2>About This Bundle</h2><p>${fullProduct.description}</p>`;
            
            if (fullProduct.what_included && fullProduct.what_included.length > 0) {
                html += `<h3>What's Included:</h3><ul>${fullProduct.what_included.map(item => `<li>${item}</li>`).join('')}</ul>`;
            }
            
            if (fullProduct.features && fullProduct.features.length > 0) {
                html += `<h3>Key Benefits:</h3><ul>${fullProduct.features.map(item => `<li>${item}</li>`).join('')}</ul>`;
            }
            
            if (fullProduct.perfect_for && fullProduct.perfect_for.length > 0) {
                html += `<h3>Perfect For:</h3><ul>${fullProduct.perfect_for.map(item => `<li>${item}</li>`).join('')}</ul>`;
            }
            
            html += `<h3>How It Works:</h3>
                <ol>
                    <li>Click the "Download Now" button</li>
                    <li>Complete the secure checkout</li>
                    <li>Get instant access to all reels</li>
                    <li>Start posting and growing your audience!</li>
                </ol>
                <p><strong>Note:</strong> This is a digital product. You will receive download links immediately after purchase.</p>`;
            
            descEl.innerHTML = html;
        }

        // Update sidebar price
        const sidebarPriceEl = document.querySelector('.price-current');
        if (sidebarPriceEl) sidebarPriceEl.textContent = `₹${fullProduct.price}`;

        const originalPriceEl = document.querySelector('.price-original');
        if (originalPriceEl && fullProduct.original_price) {
            originalPriceEl.textContent = `₹${fullProduct.original_price}`;
        }

        const sidebarDiscountEl = document.querySelector('.sidebar-discount');
        if (sidebarDiscountEl && fullProduct.discount_percentage > 0) {
            sidebarDiscountEl.textContent = `${fullProduct.discount_percentage}% OFF - Limited Time!`;
        }

        // Update checkout links to use dynamic checkout page
        document.querySelectorAll('a[href*="checkout"], .product-download-btn, .sidebar-download-btn, #productDownloadBtn, #sidebarDownloadBtn').forEach(link => {
            link.href = `/checkout.html?slug=${fullProduct.slug}`;
        });

        // Update related products - use dynamic product page
        if (fullProduct.related_products && fullProduct.related_products.length > 0) {
            const relatedList = document.querySelector('.related-products-list') || document.getElementById('relatedProductsList');
            if (relatedList) {
                relatedList.innerHTML = fullProduct.related_products.map(related => 
                    `<li><a href="product.html?slug=${related.slug}">${related.name}</a></li>`
                ).join('');
            }
        }

        // Update tags
        if (fullProduct.tags && fullProduct.tags.length > 0) {
            const tagsContainer = document.querySelector('.product-tags');
            if (tagsContainer) {
                tagsContainer.innerHTML = fullProduct.tags.map(tag => 
                    `<span class="tag">${tag.name}</span>`
                ).join('');
            }
        }

        // Store product data for checkout
        window.currentProduct = fullProduct;

    } catch (error) {
        console.error('Error loading product details:', error);
        const mainContent = document.querySelector('.product-main');
        if (mainContent) {
            mainContent.innerHTML = `
                <div style="text-align: center; padding: 3rem;">
                    <h2>Error Loading Product</h2>
                    <p>There was an error loading the product details. Please try again later.</p>
                    <a href="../index.html" style="color: #003a12; text-decoration: underline;">Go back to homepage</a>
                </div>
            `;
        }
    }
}

/**
 * Render checkout page with product data
 */
async function renderCheckoutPage(productSlug) {
    try {
        // Get product data
        const products = await api.getProducts({ search: productSlug });
        const productList = products.results || products;
        const product = productList.find(p => p.slug === productSlug);
        
        if (!product) {
            console.error('Product not found for checkout:', productSlug);
            return;
        }

        // Get full product details
        const fullProduct = await api.getProduct(product.id);

        // Update page title
        document.title = `Checkout - ${fullProduct.name} | Skilcart`;

        // Update product info
        const productTitle = document.querySelector('.checkout-product-title');
        if (productTitle) productTitle.textContent = fullProduct.name;

        const productDesc = document.querySelector('.product-desc-text');
        if (productDesc) {
            productDesc.textContent = fullProduct.short_description || fullProduct.description.substring(0, 200);
        }

        // Update product image
        const productImg = document.querySelector('.checkout-product-img-wrapper');
        if (productImg) {
            if (fullProduct.display_image) {
                productImg.innerHTML = `<img src="${fullProduct.display_image}" alt="${fullProduct.name}" style="width: 100%; height: 100%; object-fit: cover; border-radius: 12px;">`;
            } else {
                productImg.innerHTML = fullProduct.name;
            }
        }

        // Update price summary
        const subtotalEl = document.querySelector('.price-summary .price-row:first-child span:last-child') || document.getElementById('checkoutSubtotal');
        if (subtotalEl && fullProduct.original_price) {
            subtotalEl.textContent = `₹${fullProduct.original_price}`;
        } else if (subtotalEl) {
            subtotalEl.textContent = `₹${fullProduct.price}`;
        }

        const discountEl = document.querySelector('.price-summary .price-row:nth-child(2) span:last-child') || document.getElementById('checkoutDiscount');
        if (discountEl && fullProduct.discount_percentage > 0) {
            discountEl.textContent = `${fullProduct.discount_percentage}% OFF`;
        } else if (discountEl) {
            discountEl.textContent = 'No discount';
        }

        const totalEl = document.querySelector('.total-row span:last-child') || document.getElementById('checkoutTotal');
        if (totalEl) {
            totalEl.textContent = `₹${fullProduct.price}`;
        }

        // Update what's inside list
        const infoList = document.querySelector('.info-list') || document.getElementById('checkoutInfoList');
        if (infoList && fullProduct.what_included && fullProduct.what_included.length > 0) {
            infoList.innerHTML = fullProduct.what_included.map(item => `
                <li>
                    <div class="check-icon"><i class="fa-solid fa-check"></i></div>
                    <span>${item}</span>
                </li>
            `).join('');
        } else if (infoList) {
            // Default items if what_included is empty
            infoList.innerHTML = `
                <li>
                    <div class="check-icon"><i class="fa-solid fa-check"></i></div>
                    <span>Instant Download Link via Email</span>
                </li>
                <li>
                    <div class="check-icon"><i class="fa-solid fa-check"></i></div>
                    <span>HD Quality Videos without Watermark</span>
                </li>
                <li>
                    <div class="check-icon"><i class="fa-solid fa-check"></i></div>
                    <span>Lifetime Access & Updates</span>
                </li>
                <li>
                    <div class="check-icon"><i class="fa-solid fa-check"></i></div>
                    <span>100% Safe & Secure Payment</span>
                </li>
            `;
        }

        // Store product data
        window.checkoutProduct = fullProduct;

    } catch (error) {
        console.error('Error loading checkout product:', error);
    }
}

/**
 * Handle checkout form submission
 */
async function handleCheckoutForm(formElement, productSlug) {
    if (!formElement) return;

    formElement.addEventListener('submit', async (e) => {
        e.preventDefault();

        const emailInput = formElement.querySelector('input[type="email"]') || document.getElementById('email');
        const phoneInput = formElement.querySelector('input[type="tel"]') || document.getElementById('phone');
        
        const email = emailInput?.value;
        const phone = phoneInput?.value;

        if (!email || !phone) {
            alert('Please fill in all required fields (Email and Phone)');
            return;
        }

        // Validate email format
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            alert('Please enter a valid email address');
            return;
        }

        try {
            // Get product - use stored product or fetch
            let product = window.checkoutProduct;
            if (!product) {
                const products = await api.getProducts({ search: productSlug });
                const productList = products.results || products;
                product = productList.find(p => p.slug === productSlug);
                
                if (!product) {
                    alert('Product not found. Please refresh the page and try again.');
                    return;
                }
                product = await api.getProduct(product.id);
            }

            // Get bump offer status
            const bumpOffer = document.querySelector('.bump-add.active');
            const bumpOfferAdded = !!bumpOffer;
            const bumpOfferPrice = bumpOfferAdded ? 99 : null;

            // Calculate total
            let totalAmount = parseFloat(product.price);
            if (bumpOfferAdded && bumpOfferPrice) {
                totalAmount += bumpOfferPrice;
            }

            // Update button state
            const submitBtn = formElement.querySelector('button[type="submit"]') || formElement.querySelector('.pay-btn');
            const originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Processing...';
            submitBtn.disabled = true;
            submitBtn.style.opacity = '0.8';

            // Create order
            const orderData = {
                email: email,
                phone: phone,
                customer_name: '',
                product: product.id,
                quantity: 1,
                bump_offer_added: bumpOfferAdded,
                bump_offer_price: bumpOfferPrice,
            };

            const order = await api.createOrder(orderData);
            
            // Store order ID
            window.lastOrderId = order.id;
            
            // Show success message
            alert(`Order created successfully!\nOrder ID: ${order.id}\nTotal: ₹${totalAmount}\n\nYou will be redirected to payment gateway...`);
            
            // Here you would typically redirect to payment gateway
            // Example: window.location.href = `payment-gateway-url?order_id=${order.id}&amount=${totalAmount}`;
            
            // For now, just reset the form
            submitBtn.innerHTML = originalText;
            submitBtn.disabled = false;
            submitBtn.style.opacity = '1';
            
        } catch (error) {
            console.error('Error creating order:', error);
            alert('Error creating order. Please check your connection and try again.');
            
            // Reset button
            const submitBtn = formElement.querySelector('button[type="submit"]') || formElement.querySelector('.pay-btn');
            if (submitBtn) {
                submitBtn.innerHTML = 'Make Payment <i class="fa-solid fa-arrow-right"></i>';
                submitBtn.disabled = false;
                submitBtn.style.opacity = '1';
            }
        }
    });
}

/**
 * Initialize product animations
 */
function initializeProductAnimations() {
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

    document.querySelectorAll('.product-card').forEach((el, index) => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = `all 0.6s ease-out ${index * 0.1}s`;
        observer.observe(el);
    });
}

/**
 * Initialize on page load
 */
document.addEventListener('DOMContentLoaded', () => {
    // Check if we're on the homepage
    const productGrid = document.getElementById('productGrid') || document.querySelector('.product-grid');
    if (productGrid && window.location.pathname.includes('index.html')) {
        // Products will be loaded by the inline script in index.html
        // This is handled separately for better control
    }

    // Check if we're on a product page
    const productMatch = window.location.pathname.match(/products\/([^\/]+)\.html/);
    if (productMatch) {
        const productSlug = productMatch[1];
        renderProductDetails(productSlug);
    }

    // Check if we're on a checkout page
    const checkoutMatch = window.location.pathname.match(/checkout\/checkout-([^\/]+)\.html/);
    if (checkoutMatch) {
        const checkoutSlug = checkoutMatch[1];
        // Load product data for checkout
        renderCheckoutPage(checkoutSlug).then(() => {
            // Setup form handler after product is loaded
            const form = document.getElementById('checkoutForm');
            if (form) {
                handleCheckoutForm(form, checkoutSlug);
            }
        });
    }
});

