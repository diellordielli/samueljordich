var carouselOptions = {
    speed: 400
}

$(document).ready(function() {
    // gets updated on resize and on page load
    var totalWidth, totalElemnts, stepWidth, navpos = 0,

        // set superscope totalWidth
        stepWidth = $(".eventinner > .eventcontainer:first").outerWidth(true);
        totalElemnts = $(".eventinner > .eventcontainer").length;
        totalWidth = (stepWidth * totalElemnts);

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
            newLeft = -(totalElemnts -1) * stepWidth;
        }

        navpos = -newLeft / stepWidth;

        $('.eventinner').animate({'margin-left': newLeft}, carouselOptions.speed);
    });

});