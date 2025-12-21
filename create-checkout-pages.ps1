# Product data (same as before but for checkouts)
$products = @(
    @{
        key = "usa-reels"
        title = "USA Reels Bundle - Premium Viral Content"
        price = "&#8377;149"
        originalPrice = "&#8377;1499"
        discount = "90% OFF"
        bumpPrice = "&#8377;49"
        bumpTitle = "Add 500+ Luxury Car Reels"
        description = "Get access to 15,000+ premium USA luxury lifestyle reels."
    },
    @{
        key = "funny-comments"
        title = "Funny Comments Reels Bundle"
        price = "&#8377;99"
        originalPrice = "&#8377;999"
        discount = "90% OFF"
        bumpPrice = "&#8377;29"
        bumpTitle = "Add 100+ Meme Templates"
        description = "Hilarious comment reaction reels for viral engagement."
    },
    @{
        key = "ai-funny-story"
        title = "AI Funny Story Reels Bundle"
        price = "&#8377;199"
        originalPrice = "&#8377;1999"
        discount = "90% OFF"
        bumpPrice = "&#8377;49"
        bumpTitle = "Add AI Voiceover Pack"
        description = "AI-generated funny stories that keep viewers hooked."
    },
    @{
        key = "prank-video"
        title = "3500 Prank Video Reels Bundle"
        price = "&#8377;249"
        originalPrice = "&#8377;2499"
        discount = "90% OFF"
        bumpPrice = "&#8377;49"
        bumpTitle = "Add 500+ Sound Effects"
        description = "Ultimate prank collection for endless laughter."
    },
    @{
        key = "ai-hot-model"
        title = "1500+ AI Hot Model Reels Bundle"
        price = "&#8377;199"
        originalPrice = "&#8377;1999"
        discount = "90% OFF"
        bumpPrice = "&#8377;49"
        bumpTitle = "Add 200+ Fashion Reels"
        description = "High-quality AI model content for fashion niches."
    },
    @{
        key = "bike-rider"
        title = "Bike Rider Reels Bundle"
        price = "&#8377;149"
        originalPrice = "&#8377;1499"
        discount = "90% OFF"
        bumpPrice = "&#8377;39"
        bumpTitle = "Add 300+ Stunt Clips"
        description = "Adrenaline-pumping bike riding reels."
    },
    @{
        key = "car-reels"
        title = "Car Reels Bundle"
        price = "&#8377;149"
        originalPrice = "&#8377;1499"
        discount = "90% OFF"
        bumpPrice = "&#8377;39"
        bumpTitle = "Add Drift Compilation"
        description = "Luxury and sports car reels for auto enthusiasts."
    },
    @{
        key = "football-reels"
        title = "Football Reels Bundle"
        price = "&#8377;99"
        originalPrice = "&#8377;999"
        discount = "90% OFF"
        bumpPrice = "&#8377;29"
        bumpTitle = "Add 50+ Goal Celebrations"
        description = "Top football moments and skills."
    },
    @{
        key = "doraemon"
        title = "1000+ Doraemon Reels Bundle"
        price = "&#8377;149"
        originalPrice = "&#8377;1499"
        discount = "90% OFF"
        bumpPrice = "&#8377;39"
        bumpTitle = "Add Cartoon Sound Effects"
        description = "Nostalgic Doraemon clips for anime lovers."
    },
    @{
        key = "ai-superhero"
        title = "1000+ AI Superhero Interview Video Clips Pack"
        price = "&#8377;199"
        originalPrice = "&#8377;1999"
        discount = "90% OFF"
        bumpPrice = "&#8377;49"
        bumpTitle = "Add Marvel vs DC Pack"
        description = "Unique AI-generated superhero interviews."
    },
    @{
        key = "pubg-gameplay"
        title = "2000+ PUBG Gameplay Reels Bundle"
        price = "&#8377;249"
        originalPrice = "&#8377;2499"
        discount = "90% OFF"
        bumpPrice = "&#8377;49"
        bumpTitle = "Add Gaming Overlay Pack"
        description = "High-kill PUBG gameplay moments."
    },
    @{
        key = "combo-bundle"
        title = "Combo Reels Bundle (All-in-One)"
        price = "&#8377;499"
        originalPrice = "&#8377;4999"
        discount = "90% OFF"
        bumpPrice = "&#8377;99"
        bumpTitle = "Add Ultimate Editing Course"
        description = "The complete package with all reels bundles included."
    }
)

# HTML Checkout Template (SuperProfile Design)
$checkoutTemplate = @'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Checkout - {{TITLE}} | Skilcart</title>
    <link rel="stylesheet" href="../../css/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <!-- FontAwesome for Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body class="checkout-body">
    <!-- Blurred Background -->
    <div class="checkout-bg" style="background-image: url('https://images.unsplash.com/photo-1611162617474-5b21e879e113?q=80&w=1974&auto=format&fit=crop');"></div>
    <div class="checkout-overlay"></div>

    <!-- Main Checkout Card -->
    <div class="checkout-card">
        <!-- Header -->
        <div class="checkout-header">
            <div class="brand-pill">
                <i class="fa-solid fa-cart-shopping"></i> SKIL<span>CART</span>
            </div>
            <div class="platform-credit">
                Built with &#10084;&#65039; on Skilcart
            </div>
        </div>

        <!-- Content Grid -->
        <div class="checkout-content">
            <!-- Left Column: Product Info -->
            <div class="product-info-col">
                <div class="checkout-product-img-wrapper" style="background: linear-gradient(135deg, #1dbf73, #003a12); border-radius: 12px; height: 300px; display: flex; align-items: center; justify-content: center; color: white; font-size: 24px; font-weight: bold; margin-bottom: 30px;">
                    {{TITLE}}
                </div>
                
                <h1 class="checkout-product-title">{{TITLE}}</h1>

                <div class="section-label">ABOUT THE PRODUCT</div>
                <div class="product-desc-text" style="color: #444; margin-bottom: 20px; line-height: 1.6;">
                    {{DESCRIPTION}} This bundle is designed to help you grow your social media presence with high-quality, viral content.
                </div>

                <div class="section-label">WHAT'S INSIDE</div>
                <ul class="info-list">
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
                </ul>
            </div>

            <!-- Right Column: Form & Payment -->
            <div class="checkout-form-col">
                <form id="checkoutForm">
                    <div class="section-label" style="margin-top: 0;">CONTACT DETAILS</div>
                    
                    <div class="form-group">
                        <label class="form-label">Email Address</label>
                        <input type="email" class="form-input" placeholder="Enter your email" required>
                    </div>

                    <div class="form-group">
                        <label class="form-label">Phone Number</label>
                        <input type="tel" class="form-input" placeholder="Enter your mobile number" required>
                    </div>

                    <!-- Bump Offer -->
                    <div class="bump-offer">
                        <div class="bump-thumb" style="background: linear-gradient(45deg, #1774ff, #00c6ff);"></div>
                        <div class="bump-content">
                            <div class="bump-title">{{BUMP_TITLE}} <span>{{BUMP_PRICE}}</span></div>
                            <div class="bump-desc">One-time offer! Add this pack to skyrocket your growth.</div>
                        </div>
                        <div class="bump-add" onclick="this.classList.toggle('active')">
                            <i class="fa-solid fa-check" style="font-size: 12px;"></i>
                        </div>
                    </div>

                    <!-- Price Summary -->
                    <div class="price-summary">
                        <div class="price-row">
                            <span>Subtotal</span>
                            <span style="text-decoration: line-through;">{{ORIGINAL_PRICE}}</span>
                        </div>
                        <div class="price-row">
                            <span>Discount</span>
                            <span style="color: #4caf50;">{{DISCOUNT}}</span>
                        </div>
                        <div class="total-row">
                            <span>Total Amount</span>
                            <span>{{PRICE}}</span>
                        </div>
                    </div>

                    <!-- Payment Button -->
                    <button type="submit" class="pay-btn">
                        Make Payment <i class="fa-solid fa-arrow-right"></i>
                    </button>

                    <div class="secure-badge">
                        <i class="fa-solid fa-lock"></i> SSL Secured Payment
                    </div>
                </form>
            </div>
        </div>
    </div>

    <!-- Simple Script for form submission demo -->
    <script>
        document.getElementById('checkoutForm').addEventListener('submit', function(e) {
            e.preventDefault();
            const btn = this.querySelector('.pay-btn');
            const originalText = btn.innerHTML;
            btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Processing...';
            btn.style.opacity = '0.8';
            
            setTimeout(() => {
                alert('Redirecting to Payment Gateway...');
                btn.innerHTML = originalText;
                btn.style.opacity = '1';
            }, 1500);
        });
    </script>
</body>
</html>
'@

# Create checkout directory if it doesn't exist
$checkoutDir = "c:\Users\utsab\OneDrive\Desktop\skillcart\html\checkout"
if (-not (Test-Path $checkoutDir)) {
    New-Item -ItemType Directory -Path $checkoutDir -Force
}

# Generate each checkout page
foreach ($product in $products) {
    if ($product.key -eq "combo-bundle") {
        $filename = "$checkoutDir\checkout-combo-bundle.html"
    } else {
        $filename = "$checkoutDir\checkout-$($product.key).html"
    }

    $html = $checkoutTemplate
    $html = $html -replace '{{TITLE}}', $product.title
    $html = $html -replace '{{PRICE}}', $product.price
    $html = $html -replace '{{ORIGINAL_PRICE}}', $product.originalPrice
    $html = $html -replace '{{DISCOUNT}}', $product.discount
    $html = $html -replace '{{BUMP_PRICE}}', $product.bumpPrice
    $html = $html -replace '{{BUMP_TITLE}}', $product.bumpTitle
    $html = $html -replace '{{DESCRIPTION}}', $product.description
    
    $html | Out-File -FilePath $filename -Encoding UTF8
    Write-Host "Created Checkout: $filename"
}

Write-Host "`nAll 12 checkout pages created successfully with SuperProfile design!"
