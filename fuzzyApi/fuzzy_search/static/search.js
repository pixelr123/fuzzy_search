$(function(){

    $('#search').keyup(function(){
        $.ajax({
            type: 'GET',
            url: 'search',
            data:{
                'word': $('#search').val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
    });
});

function searchSuccess(data, textStatus, jqXHR)
{
    $('#search-results').html(data);
}