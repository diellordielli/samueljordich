var carouselOptions = {
    speed: 400,
    imageRatio: 0.67,
    imageRatioH: 0.435
}

$(document).ready(function() {
    // gets updated on resize and on page load
    var totalWidth, totalImages, stepWidth, navpos = 0,

        // set superscope totalWidth
        stepWidth = $(".archiveinner > .archivecontainer:first").outerWidth(true);
        totalImages = $(".archiveinner > .archivecontainer").length;
        totalWidth = (stepWidth * totalImages);

        $(".archiveinner").width(totalWidth);

        $('.archiveinner').css('margin-left', - navpos * stepWidth);

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