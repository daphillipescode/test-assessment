$('#contactForm').on('submit', function(e){
    var form = new FormData(this);
    $.ajax({
        url: '',
        type: 'POST',
        data: form,
        success: function(response){
            if(response.data == 'success'){
                $('#alertDiv').html(
                `<div class='alert alert-success'>&emsp; Successfully Sent.</div>`
                )
                $('#contactForm').trigger('reset');
            } else {
                var msg = response.msg;
                for(var i = 0; i < msg.length; i++){
                    $('#alertDiv').append(
                        `<div class='alert alert-danger'>&emsp;` +
                            msg[i]
                        + `</div>`
                    );
                }
            }
        },
        cache: false,
        contentType: false,
        processData: false,
    });

    e.preventDefault();
})

$('#animals').on('change', function(){
    var animals = $(this).val();
    var status = false;
    for(var i = 0; i < animals.length; i++){
        if(animals[i] == 'tiger'){
            status = true
        }
    }

    if(status){
        $('#type-content').removeClass('display-none');
        $('#type').attr('required', true);
    } else {
        $('#type-content').addClass('display-none');
        $('#type').attr('required', false);
    }
});