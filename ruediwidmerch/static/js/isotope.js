$(function(){

    var $container = $('#container');
  
    $container.isotope({
        itemSelector: '.item',
        masonry: {
            columnWidth: 60
        }
    })

    $('.item.portrait').click(function(){
        var $this = $(this),
            tileStyle = $this.hasClass('big');
        $this.toggleClass('big');

        $this.find('.portraitdesc').toggle();
        $this.find('.portraitsubtitle').toggle();
        $this.find('.portraittitle').toggleClass('portraittitle2');
        $container.isotope( 'reLayout' )

    });
});