$(function(){
  var $container = $('#container');
  
  $container.isotope({
    itemSelector: '.item',
    masonry: {
      columnWidth: 60
    }
  })
  
  var $container = $('#container');
  
  $container.isotope({
    itemSelector: '.item',
    masonry: {
      columnWidth: 60
    }
  })
  
  $('.item').click(function(){
    var $this = $(this),
        tileStyle = $this.hasClass('big') ? { width: 50, height: 50} : { width: 170, height: 110};
    $this.toggleClass('big');
    
    $this.find('.portraitdesc').toggle();
    $this.find('.portraitsubtitle').toggle();
    $this.find('.portraittitle').toggleClass('portraittitle2');
    $container.isotope( 'reLayout' )
    
  });
});
