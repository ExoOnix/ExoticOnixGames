function clickred() {
$.ajax({
    type: 'POST',
    url: 'colorclicker/clickred',
    dataType: 'html'
});
}

function clickblue() {
$.ajax({
    type: 'POST',
    url: 'colorclicker/clickblue',
    dataType: 'html'
});

}


function reloadred() {
    $.get("/colorclicker/getred", function(data) {
    $("#getred").html(data);

    });
}

function reloadblue() {
    $.get("/colorclicker/getblue", function(data) {
    $("#getblue").html(data);

    });
}

$(function(){
setInterval(reloadred, 5000);
setInterval(reloadblue, 5000);
});