var carouselOptions = {
    speed: 400,
    imageRatio: 0.67,
    imageRatioH: 0.435
}

$(document).ready(function() {
    // gets updated on resize and on page load
    var totalWidth, totalImages, stepWidth, navpos = 0,

        // set superscope totalWidth
        stepWidth = $(".eventinner > .eventcontainer:first").outerWidth(true);
        totalImages = $(".eventinner > .eventcontainer").length;
        totalWidth = (stepWidth * totalImages);

        $(".eventinner").width(totalWidth);

        $('.eventinner').css('margin-left', - navpos * stepWidth);

    $('.navright').on('click', function(event) {
        event.preventDefault();
        var newLeft = $('.eventinner').get(0).offsetLeft - stepWidth;

        if (newLeft <= -totalWidth) {
            newLeft = 0;
        }

        navpos = -newLeft / stepWidth;

        $('.eventinner').animate({'margin-left': newLeft}, carouselOptions.speed);

    });

    $('.navleft').on('click', function(event) {
        event.preventDefault();
        var newLeft = $('.eventinner').get(0).offsetLeft + stepWidth;

        if (newLeft > 0) {
            newLeft = -(totalImages -1) * stepWidth;
        }

        navpos = -newLeft / stepWidth;

        $('.eventinner').animate({'margin-left': newLeft}, carouselOptions.speed);
    });

});