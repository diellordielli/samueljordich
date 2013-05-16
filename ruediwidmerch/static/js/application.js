$(document).ready(function() {

    $('#acartoon').on('mouseover', function(event) {
        $('#acartoon a').hide();
        $('#cartoonimg').css({'display':'inline'});
    });

    $('#cartoonimg').on('mouseleave', function(event) {
        $('#cartoonimg').hide();
        $('#acartoon a').css({'display':'inline'});
    });

    $('#atexte').on('mouseover', function(event) {
        $('#atexte a').hide();
        $('#texteimg').css({'display':'inline'});
    });

    $('#texteimg').on('mouseleave', function(event) {
        $('#texteimg').hide();
        $('#atexte a').css({'display':'inline'});
    });

    $('#anews').on('mouseover', function(event) {
        $('#anews a').hide();
        $('#newsimg').css({'display':'inline'});
    });

    $('#newsimg').on('mouseleave', function(event) {
        $('#newsimg').hide();
        $('#anews a').css({'display':'inline'});
    });

    $('#aportrait').on('mouseover', function(event) {
        $('#aportrait a').hide();
        $('#portraitimg').css({'display':'inline'});
    });

    $('#portraitimg').on('mouseleave', function(event) {
        $('#portraitimg').hide();
        $('#aportrait a').css({'display':'inline'});
    });

    $('#akontakt').on('mouseover', function(event) {
        $('#akontakt a').hide();
        $('#kontaktimg').css({'display':'inline'});
    });

    $('#kontaktimg').on('mouseleave', function(event) {
        $('#kontaktimg').hide();
        $('#akontakt a').css({'display':'inline'});
    });


});