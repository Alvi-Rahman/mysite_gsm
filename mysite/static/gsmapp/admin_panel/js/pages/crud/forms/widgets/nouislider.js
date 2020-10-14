// Class definition
var KTnoUiSliderDemos = function() {

    // Private functions


    var user = function() {
        // init slider
        var slider = document.getElementById('kt_nouislider_user');

        noUiSlider.create(slider, {
            start: [ 1 ],
            connect: [true, false],
            step: 1,
            range: {
                'min': [ 1 ],
                'max': [ 25 ]
            },
            format: wNumb({
                decimals: 3,
                thousand: '.',
                postfix: " User"
            })
        });

        // init slider input
        var sliderInput = document.getElementById('kt_nouislider_user_input');

        slider.noUiSlider.on('update', function( values, handle ) {
            sliderInput.value = values[handle];
            price_calculation(values);
        });

        sliderInput.addEventListener('change', function(){
            slider.noUiSlider.set(this.value);
        });
    }

    var duration = function() {
        // init slider
        var slider = document.getElementById('kt_nouislider_duration');

        noUiSlider.create(slider, {
            start: [ 0 ],
            connect: [true, false],
            step: 1,
            range: {
                'min': [ 1 ],
                'max': [ 60 ]
            },
            format: wNumb({
                decimals: 3,
                thousand: '.',
                postfix: " Month"
            })
        });

        // init slider input
        var sliderInput = document.getElementById('kt_nouislider_duration_input');

        slider.noUiSlider.on('update', function( values, handle ) {
            sliderInput.value = values[handle];
            price_calculation(values);
        });

        sliderInput.addEventListener('change', function(){
            slider.noUiSlider.set(this.value);
        });
    }

    var facebook_page = function() {
        // init slider
        var slider = document.getElementById('kt_nouislider_facebook_page');

        noUiSlider.create(slider, {
            start: [ 1 ],
            connect: [true, false],
            step: 1,
            range: {
                'min': [ 0 ],
                'max': [ 25 ]
            },
            format: wNumb({
                decimals: 3,
                thousand: '.',
                postfix: " Facebook Page"
            })
        });

        // init slider input
        var sliderInput = document.getElementById('kt_nouislider_facebook_page_input');

        slider.noUiSlider.on('update', function( values, handle ) {
            sliderInput.value = values[handle];
            price_calculation(values);
        });

        sliderInput.addEventListener('change', function(){ 
            slider.noUiSlider.set(this.value);
        });
    }

    var instagram_account = function() {
        // init slider
        var slider = document.getElementById('kt_nouislider_instagram_account');

        noUiSlider.create(slider, {
            start: [ 0 ],
            connect: [true, false],
            step: 1,
            range: {
                'min': [ 0 ],
                'max': [ 25 ]
            },
            format: wNumb({
                decimals: 3,
                thousand: '.',
                postfix: " Instagram"
            })
        });

        // init slider input
        var sliderInput = document.getElementById('kt_nouislider_instagram_account_input');

        slider.noUiSlider.on('update', function( values, handle ) {
            sliderInput.value = values[handle];
            price_calculation(values);
        });

        sliderInput.addEventListener('change', function(){
            slider.noUiSlider.set(this.value);
        });
    }

    var twitter_account = function() {
        // init slider
        var slider = document.getElementById('kt_nouislider_twitter_account');

        noUiSlider.create(slider, {
            start: [ 0 ],
            connect: [true, false],
            step: 1,
            range: {
                'min': [ 0 ],
                'max': [ 25 ]
            },
            format: wNumb({
                decimals: 3,
                thousand: '.',
                postfix: " Twitter"
            })
        });

        // init slider input
        var sliderInput = document.getElementById('kt_nouislider_twitter_account_input');

        slider.noUiSlider.on('update', function( values, handle ) {
            sliderInput.value = values[handle];
            price_calculation(values);
        });

        sliderInput.addEventListener('change', function(){
            slider.noUiSlider.set(this.value);
        });
    }

    var youtube_account = function() {
        // init slider
        var slider = document.getElementById('kt_nouislider_youtube_account');

        noUiSlider.create(slider, {
            start: [ 0 ],
            connect: [true, false],
            step: 1,
            range: {
                'min': [ 0 ],
                'max': [ 25 ]
            },
            format: wNumb({
                decimals: 3,
                thousand: '.',
                postfix: " Youtube"
            })
        });

        // init slider input
        var sliderInput = document.getElementById('kt_nouislider_youtube_account_input');

        slider.noUiSlider.on('update', function( values, handle ) {
            sliderInput.value = values[handle];
            price_calculation(values);
        });

        sliderInput.addEventListener('change', function(){
            slider.noUiSlider.set(this.value);
        });
    }

    var linkedIn_account = function() {
        // init slider
        var slider = document.getElementById('kt_nouislider_linkedIn_account');

        noUiSlider.create(slider, {
            start: [ 0 ],
            connect: [true, false],
            step: 1,
            range: {
                'min': [ 0 ],
                'max': [ 25 ]
            },
            format: wNumb({
                decimals: 3,
                thousand: '.',
                postfix: " LinkedIn"
            })
        });

        // init slider input
        var sliderInput = document.getElementById('kt_nouislider_linkedIn_account_input');

        slider.noUiSlider.on('update', function( values, handle ) {
            sliderInput.value = values[handle];
            price_calculation(values);
        });

        sliderInput.addEventListener('change', function(){
            slider.noUiSlider.set(this.value);
        });
    }
    
    return {
        // public functions
        init: function() {
            try {
                user();
            }
            catch{}
            try {
                duration();
            }
            catch{}
            try {
                facebook_page();  
            }
            catch{}
            try {
                instagram_account();    
            }
            catch{}
            try {
                twitter_account();     
            }
            catch{}                     
            try {
                youtube_account();     
            }
            catch{}                     
            try {
                linkedIn_account();     
            }
            catch{}                     
        }
    };
}();

jQuery(document).ready(function() {
    KTnoUiSliderDemos.init();
});


