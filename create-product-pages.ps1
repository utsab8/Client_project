# Product data
$products = @(
    @{
        key = "usa-reels"
        title = "USA Reels Bundle"
        price = "&#8377;149"
        originalPrice = "&#8377;1499"
        discount = "90% OFF"
        count = "15,000+"
        description = "USA luxury lifestyle reels"
        checkoutUrl = "checkout-usa-reels.html"
    },
    @{
        key = "funny-comments"
        title = "Funny Comments Reels Bundle"
        price = "&#8377;99"
        originalPrice = "&#8377;999"
        discount = "90% OFF"
        count = "500+"
        description = "hilarious reaction reels"
        checkoutUrl = "checkout-funny-comments.html"
    },
    @{
        key = "ai-funny-story"
        title = "AI Funny Story Reels Bundle"
        price = "&#8377;199"
        originalPrice = "&#8377;1999"
        discount = "90% OFF"
        count = "800+"
        description = "AI-generated funny stories"
        checkoutUrl = "checkout-ai-funny-story.html"
    },
    @{
        key = "prank-video"
        title = "3500 Prank Video Reels Bundle"
        price = "&#8377;249"
        originalPrice = "&#8377;2499"
        discount = "90% OFF"
        count = "3500+"
        description = "prank clips for instant laughs"
        checkoutUrl = "checkout-prank-video.html"
    },
    @{
        key = "ai-hot-model"
        title = "1500+ AI Hot Model Reels Bundle"
        price = "&#8377;199"
        originalPrice = "&#8377;1999"
        discount = "90% OFF"
        count = "1500+"
        description = "AI-generated model reels"
        checkoutUrl = "checkout-ai-hot-model.html"
    },
    @{
        key = "bike-rider"
        title = "Bike Rider Reels Bundle"
        price = "&#8377;149"
        originalPrice = "&#8377;1499"
        discount = "90% OFF"
        count = "1000+"
        description = "thrilling bike riding reels"
        checkoutUrl = "checkout-bike-rider.html"
    },
    @{
        key = "car-reels"
        title = "Car Reels Bundle"
        price = "&#8377;149"
        originalPrice = "&#8377;1499"
        discount = "90% OFF"
        count = "1000+"
        description = "luxury car reels"
        checkoutUrl = "checkout-car-reels.html"
    },
    @{
        key = "football-reels"
        title = "Football Reels Bundle"
        price = "&#8377;99"
        originalPrice = "&#8377;999"
        discount = "90% OFF"
        count = "800+"
        description = "top football moments"
        checkoutUrl = "checkout-football-reels.html"
    },
    @{
        key = "doraemon"
        title = "1000+ Doraemon Reels Bundle"
        price = "&#8377;149"
        originalPrice = "&#8377;1499"
        discount = "90% OFF"
        count = "1000+"
        description = "anime clips pack"
        checkoutUrl = "checkout-doraemon.html"
    },
    @{
        key = "ai-superhero"
        title = "1000+ AI Superhero Interview Video Clips Pack"
        price = "&#8377;199"
        originalPrice = "&#8377;1999"
        discount = "90% OFF"
        count = "1000+"
        description = "AI superhero interviews"
        checkoutUrl = "checkout-ai-superhero.html"
    },
    @{
        key = "pubg-gameplay"
        title = "2000+ PUBG Gameplay Reels Bundle"
        price = "&#8377;249"
        originalPrice = "&#8377;2499"
        discount = "90% OFF"
        count = "2000+"
        description = "gaming clips for shorts"
        checkoutUrl = "checkout-pubg-gameplay.html"
    },
    @{
        key = "combo-bundle"
        title = "Combo Reels Bundle"
        price = "&#8377;499"
        originalPrice = "&#8377;4999"
        discount = "90% OFF"
        count = "All"
        description = "complete bundle package"
        checkoutUrl = "checkout-combo-bundle.html"
    }
)

# HTML template
$template = @'
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{{TITLE}} - Premium viral content for social media growth">
    <title>{{TITLE}} - Skilcart</title>
    <link rel="stylesheet" href="../../css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@300;400;500;600;700&display=swap"
        rel="stylesheet">
</head>

<body>
    <!-- Header -->
    <header class="header">
        <div class="header-top">
            <div class="container header-top-inner">
                <div class="logo">
                    <a href="../index.html">SKIL<span>CART</span></a>
                </div>
                <nav class="top-nav">
                    <ul>
                        <li><a href="../index.html">Home</a></li>
                        <li><a href="https://wa.me/919712237383" target="_blank">WhatsApp</a></li>
                        <li><a href="../index.html#reels-bundle">Reels Bundle</a></li>
                    </ul>
                </nav>
            </div>
        </div>

        <div class="header-bottom">
            <div class="container header-bottom-inner">
                <button class="mobile-menu-toggle" id="mobileMenuToggle">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
                <nav class="nav" id="mainNav">
                    <ul class="nav-list">
                        <li><a href="../index.html">Home</a></li>
                        <li><a href="../index.html#reels-bundle">Combo Reels bundle</a></li>
                        <li><a href="../index.html#reels-bundle">Instagram Reels Bundle</a></li>
                        <li><a href="../index.html?price=99">Reels bundle &#8377;99</a></li>
                        <li><a href="../index.html?price=149">Reels bundle &#8377;149</a></li>
                        <li><a href="../index.html?price=199">Reels bundle &#8377;199</a></li>
                        <li><a href="../index.html?price=249">Reels bundle &#8377;249</a></li>
                    </ul>
                </nav>
            </div>
        </div>
    </header>

    <!-- Product Page Content -->
    <main class="product-page">
        <div class="container">
            <div class="product-layout">
                <!-- Main Content Column -->
                <div class="product-main">
                    <!-- Breadcrumb -->
                    <nav class="breadcrumb">
                        <a href="../index.html">Home</a> &gt; 
                        <a href="../index.html#reels-bundle">Reels Bundle</a> &gt; 
                        <span>{{TITLE}}</span>
                    </nav>

                    <!-- Product Title -->
                    <h1 class="product-page-title">{{TITLE}}</h1>

                    <!-- Brand Tag -->
                    <div class="product-brand">
                        <span>&#128193; Skilcart</span>
                    </div>

                    <!-- Product Image -->
                    <div class="product-featured-image">
                        <div class="product-banner-placeholder" style="background: linear-gradient(135deg, #1dbf73, #003a12); color: white; display: flex; align-items: center; justify-content: center; height: 400px; font-size: 2rem; font-weight: 700; border-radius: 8px;">
                            {{TITLE}}
                        </div>
                    </div>

                    <!-- Action Bar (Price + Download) -->
                    <div class="product-action-bar">
                        <div class="product-price-info">
                            <div class="product-price">{{PRICE}}</div>
                            <div class="product-discount">{{DISCOUNT}}</div>
                        </div>
                        <a href="../checkout/{{CHECKOUT_URL}}" class="product-download-btn">
                            &#127775; Download Now
                        </a>
                    </div>

                    <!-- Product Description -->
                    <div class="product-description">
                        <h2>About This Bundle</h2>
                        <p>Get access to {{COUNT}} premium {{DESCRIPTION}} perfect for viral social media growth. This comprehensive bundle includes high-quality, ready-to-post content that will save you hours of content creation time.</p>
                        
                        <h3>What's Included:</h3>
                        <ul>
                            <li>{{COUNT}} {{DESCRIPTION}}</li>
                            <li>HD quality videos ready to post</li>
                            <li>Trending content for maximum engagement</li>
                            <li>Instant download access</li>
                            <li>Lifetime updates</li>
                        </ul>

                        <h3>Key Benefits:</h3>
                        <ul>
                            <li>&#128293; Premium trending content</li>
                            <li>&#9201; Save hours of content creation</li>
                            <li>&#128514; Boost engagement and watch time</li>
                            <li>&#128640; Grow your following fast</li>
                            <li>&#128176; Affordable pricing with {{DISCOUNT}}</li>
                        </ul>

                        <h3>Perfect For:</h3>
                        <ul>
                            <li>Instagram Reels creators</li>
                            <li>YouTube Shorts channels</li>
                            <li>TikTok content creators</li>
                            <li>Social media managers</li>
                            <li>Digital marketers</li>
                        </ul>

                        <h3>How It Works:</h3>
                        <ol>
                            <li>Click the "Download Now" button</li>
                            <li>Complete the secure checkout</li>
                            <li>Get instant access to all {{COUNT}} reels</li>
                            <li>Start posting and growing your audience!</li>
                        </ol>

                        <p><strong>Note:</strong> This is a digital product. You will receive download links immediately after purchase.</p>
                    </div>
                </div>

                <!-- Sidebar Column -->
                <aside class="product-sidebar">
                    <!-- Pricing Widget -->
                    <div class="sidebar-widget pricing-widget">
                        <h3>Get This Bundle</h3>
                        <div class="sidebar-price">
                            <span class="price-current">{{PRICE}}</span>
                            <span class="price-original">{{ORIGINAL_PRICE}}</span>
                        </div>
                        <div class="sidebar-discount">{{DISCOUNT}} - Limited Time!</div>
                        <a href="../checkout/{{CHECKOUT_URL}}" class="sidebar-download-btn">
                            &#127775; Download Now
                        </a>
                        <div class="sidebar-features">
                            <div class="feature-item">&#10003; Instant Download</div>
                            <div class="feature-item">&#10003; Lifetime Access</div>
                            <div class="feature-item">&#10003; {{COUNT}} Reels</div>
                            <div class="feature-item">&#10003; HD Quality</div>
                        </div>
                    </div>

                    <!-- Related Products Widget -->
                    <div class="sidebar-widget related-widget">
                        <h3>Get Epic Viral Reels Bundle</h3>
                        <ul class="related-products-list">
                            <li><a href="usa-reels-bundle.html">USA Reels Bundle</a></li>
                            <li><a href="funny-comments-bundle.html">Funny Comments Reels Bundle</a></li>
                            <li><a href="ai-funny-story-bundle.html">AI Funny Story Reels Bundle</a></li>
                            <li><a href="prank-video-bundle.html">3500 Prank Video Reels Bundle</a></li>
                            <li><a href="combo-bundle.html">Combo Reels Bundle (All-in-One)</a></li>
                        </ul>
                    </div>

                    <!-- Tags Widget -->
                    <div class="sidebar-widget tags-widget">
                        <h3>Tags</h3>
                        <div class="product-tags">
                            <span class="tag">Reels Bundle</span>
                            <span class="tag">Viral Content</span>
                            <span class="tag">Instagram Reels</span>
                            <span class="tag">Social Media</span>
                            <span class="tag">Content Bundle</span>
                        </div>
                    </div>
                </aside>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>SKILCART</h3>
                    <p>Best Digital Product In India</p>
                </div>
                <div class="footer-section">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="../index.html">Home</a></li>
                        <li><a href="#">About Us</a></li>
                        <li><a href="#">Privacy Policy</a></li>
                        <li><a href="#">Terms &amp; Conditions</a></li>
                        <li><a href="#">Refund Policy</a></li>
                        <li><a href="#">Contact Us</a></li>
                        <li><a href="#">Digital Planner 2025</a></li>
                        <li><a href="../index.html#reels-bundle">Reels Bundle</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Connect</h4>
                    <div class="footer-social">
                        <a href="https://instagram.com/mr_sebby_yt" target="_blank">Instagram</a>
                        <a href="https://wa.me/919712237383" target="_blank">WhatsApp</a>
                        <a href="https://youtube.com/@mr_sebby?si=cKM9OKvrKpDiuMq-" target="_blank">YouTube</a>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2023 Skil Cart All Right Reserved</p>
            </div>
        </div>
    </footer>

    <script src="../../js/script.js"></script>
</body>

</html>
'@

# Create products directory if it doesn't exist
$productsDir = "c:\Users\utsab\OneDrive\Desktop\skillcart\html\products"
if (-not (Test-Path $productsDir)) {
    New-Item -ItemType Directory -Path $productsDir -Force
}

# Generate each product page
foreach ($product in $products) {
    $html = $template
    $html = $html -replace '{{TITLE}}', $product.title
    $html = $html -replace '{{PRICE}}', $product.price
    $html = $html -replace '{{ORIGINAL_PRICE}}', $product.originalPrice
    $html = $html -replace '{{DISCOUNT}}', $product.discount
    $html = $html -replace '{{COUNT}}', $product.count
    $html = $html -replace '{{DESCRIPTION}}', $product.description
    $html = $html -replace '{{CHECKOUT_URL}}', $product.checkoutUrl
    
    if ($product.key -eq "combo-bundle") {
        $filename = "$productsDir\$($product.key).html"
    } else {
        $filename = "$productsDir\$($product.key)-bundle.html"
    }
    $html | Out-File -FilePath $filename -Encoding UTF8
    Write-Host "Created: $filename"
}

Write-Host "`nAll 12 product pages created successfully!"
