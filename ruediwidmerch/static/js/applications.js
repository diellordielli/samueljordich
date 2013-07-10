$(document).ready(function() {

    $('.supernews img').css({'height': '100px'});

    $('.item.category').mouseenter(function() {
        var $this = $(this);

        $this.find('span').css({'color': '#000'});
    });

    $('.item.category').mouseleave(function() {
        var $this = $(this);

        $this.find('span').css({'color': '#FFF'});
    });

});