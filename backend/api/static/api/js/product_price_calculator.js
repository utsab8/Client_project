/**
 * Product Price Calculator for Django Admin
 * Automatically calculates discounted price when original price or discount percentage changes
 */

(function($) {
    'use strict';
    
    $(document).ready(function() {
        // Get the form fields
        var $originalPrice = $('#id_original_price');
        var $discountPercentage = $('#id_discount_percentage');
        var $price = $('#id_price');
        
        // Function to calculate price
        function calculatePrice() {
            var originalPrice = parseFloat($originalPrice.val()) || 0;
            var discountPercentage = parseFloat($discountPercentage.val()) || 0;
            
            if (originalPrice > 0 && discountPercentage >= 0 && discountPercentage <= 100) {
                var discountAmount = (originalPrice * discountPercentage) / 100;
                var discountedPrice = originalPrice - discountAmount;
                
                // Round to 2 decimal places
                discountedPrice = Math.round(discountedPrice * 100) / 100;
                
                // Update the price field
                $price.val(discountedPrice.toFixed(2));
                
                // Add visual feedback
                $price.css({
                    'background-color': '#d4edda',
                    'transition': 'background-color 0.3s'
                });
                
                setTimeout(function() {
                    $price.css('background-color', '');
                }, 500);
            } else if (originalPrice > 0 && discountPercentage === 0) {
                // No discount, price equals original
                $price.val(originalPrice.toFixed(2));
            }
        }
        
        // Calculate on input change
        $originalPrice.on('input change', calculatePrice);
        $discountPercentage.on('input change', calculatePrice);
        
        // Calculate on page load if values exist
        if ($originalPrice.val() && $discountPercentage.val()) {
            calculatePrice();
        }
        
        // Add helper text display
        if ($originalPrice.length && $discountPercentage.length && $price.length) {
            // Create info display
            var $infoDiv = $('<div>', {
                id: 'price-calculator-info',
                css: {
                    'margin-top': '10px',
                    'padding': '10px',
                    'background-color': '#e7f3ff',
                    'border-left': '4px solid #2196F3',
                    'border-radius': '4px',
                    'font-size': '13px',
                    'color': '#333'
                }
            });
            
            // Insert after discount percentage field
            $discountPercentage.closest('.form-row').after($infoDiv);
            
            // Update info display
            function updateInfo() {
                var originalPrice = parseFloat($originalPrice.val()) || 0;
                var discountPercentage = parseFloat($discountPercentage.val()) || 0;
                var price = parseFloat($price.val()) || 0;
                
                if (originalPrice > 0 && discountPercentage > 0) {
                    var discountAmount = (originalPrice * discountPercentage) / 100;
                    $infoDiv.html(
                        '<strong>Calculation:</strong> ₹' + originalPrice.toFixed(2) + 
                        ' - (₹' + originalPrice.toFixed(2) + ' × ' + discountPercentage + '%) = ' +
                        '<strong>₹' + price.toFixed(2) + '</strong> ' +
                        '<span style="color: #4caf50;">(Save ₹' + discountAmount.toFixed(2) + ')</span>'
                    );
                } else if (originalPrice > 0) {
                    $infoDiv.html(
                        '<strong>Price:</strong> ₹' + originalPrice.toFixed(2) + 
                        ' (No discount applied)'
                    );
                } else {
                    $infoDiv.html('Enter Original Price and Discount Percentage to calculate discounted price.');
                }
            }
            
            // Update info on change
            $originalPrice.on('input change', updateInfo);
            $discountPercentage.on('input change', updateInfo);
            
            // Initial update
            updateInfo();
        }
    });
})(django.jQuery);

