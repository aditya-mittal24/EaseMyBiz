$('.selectall').click(function() {
    if ($(this).is(':checked')) {
        $('div input').attr('checked', true);
        console.log("clicked");
    } else {
        $('div input').attr('checked', false);
    }
});