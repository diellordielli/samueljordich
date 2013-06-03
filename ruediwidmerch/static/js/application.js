$(document).ready(function() {

    $('.navright2').on('click', function(event) {
        $('navleft2').parent().css('background-color', 'red');
    });

    $('.navright2').on('click', function(event) {
        var currentHeight,
            newsindex = $('.archiveouter').data('textindex'),
            $currentColumn = $('.archivecontainer').eq(newsindex);

        currentHeight = $currentColumn.outerHeight();

        //$('.archiveouter').animate({'height': currentHeight});

    });

    $('.navleft2').on('click', function(event) {
        var currentHeight,
            newsindex = $('.archiveouter').data('textindex'),
            $currentColumn = $('.archivecontainer').eq(newsindex);

        currentHeight = $currentColumn.outerHeight();

        //$('.archiveouter').animate({'height': currentHeight});

    });

});