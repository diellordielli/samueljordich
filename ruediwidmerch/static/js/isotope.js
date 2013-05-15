$(function(){
    $('#container').isotope({
        itemSelector : '.item',
        masonry: {
            columnWidth: 60,
            cornerStampSelector: '.corner-stamp'
        },
        animationOptions: {
            duration: 750,
            easing: 'linear',
            queue: false
        }
    });
});