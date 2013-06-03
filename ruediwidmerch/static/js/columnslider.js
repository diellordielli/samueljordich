var carouselOptions = {
    speed: 400,
    imageRatio: 1,
    imageRatioH: 0.435
}

$(document).ready(function() {
    // gets updated on resize and on page load
    var totalWidth, totalImages, stepWidth, navpos = 0
        $archiveouter = $('.archiveouter');

    resize();

    $(window).resize(function() {
        resize();
    });

    function resize() {
        var regionGrey = $('.archiveall').width(),
            newsWidth = Math.round(regionGrey * carouselOptions.imageRatio);

        $('.archivecontainer').width(newsWidth);

        var marginleft = (regionGrey - newsWidth) / 2;
        $('.archivecontainer').css('margin-left', marginleft + 'px');

        var marginright = (regionGrey - newsWidth) / 2;
        $('.archivecontainer').css('margin-right', marginright + 'px');

        // set superscope totalWidth
        stepWidth = $(".archiveinner > .archivecontainer:first").outerWidth(true);
        totalImages = $(".archiveinner > .archivecontainer").length;
        totalWidth = (stepWidth * totalImages);

        $(".archiveinner").width(totalWidth);

        $('.archiveinner').css('margin-left', - navpos * stepWidth);
    }

    for (var i = 1; i < totalImages; i++){
        $archiveouter.clone().data('textindex', i); 
    }

    $archiveouter.addClass('active');

    $('.navright2').on('click', function(event) {
        event.preventDefault();
        var newLeft = $('.archiveinner').get(0).offsetLeft - stepWidth;

        if (newLeft <= -totalWidth) {
            newLeft = 0;
        }

        navpos = -newLeft / stepWidth;

        $('.archiveinner').animate({'margin-left': newLeft}, carouselOptions.speed);

    });

    $('.navleft2').on('click', function(event) {
        event.preventDefault();
        var newLeft = $('.archiveinner').get(0).offsetLeft + stepWidth;

        if (newLeft > 0) {
            newLeft = -(totalImages -1) * stepWidth;
        }

        navpos = -newLeft / stepWidth;

        $('.archiveinner').animate({'margin-left': newLeft}, carouselOptions.speed);
    });

});