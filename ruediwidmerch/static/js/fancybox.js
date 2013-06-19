$(document).ready(function() {
    /*$(".fancybox").fancybox({
        type: 'ajax'
    });*/

    $('.fancybox').on('click', function(event) {
        event.preventDefault();

        var $this = $(this);

        // Get on screen image
        var screenImage = $this.find('img');

        // Create new offscreen image to test
        var theImage = new Image();
        theImage.src = screenImage.attr("src");

        // Get accurate measurements from that.
        var imageWidth = theImage.width;
        var imageHeight = theImage.height;

        console.log(imageWidth, imageHeight);

        $.fancybox(this, {type: 'ajax'});
        $.fancybox({'width': imageWidth, 'height': imageHeight});
    });
});