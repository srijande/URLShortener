function copyToClipboard(element) {
	console.log('function is running!');
	console.log($(element).val())
	var $temp = $("<input>");
	$("body").append($temp);
	$temp.val($(element).val()).select();
	document.execCommand("copy");
	$temp.remove();
	$("#copyButton").val('Copied!');
}

$(document).ready(function(){
	
	const colors = document.getElementsByClassName('theme');


	let i;
	for(i=0;i<colors.length;i++) {
		colors[i].addEventListener('click', changeColor); 
	}

	function changeColor() {
		let color = this.getAttribute('data-color');
		
		document.documentElement.style.setProperty('--color', color);
	}
  });



$("#url").on('keyup', function(){
	$("#copyButton").val('Copy');
	$("#shortenButton").css("display", "block");
	$("#copyButton").css("display", "none");
  });
 
$(document).on('submit', '#post-form',function(e){
	e.preventDefault();
    $.ajax({
        type:'POST',
        url:'short/create_post',
        data:{
            url:$('#url').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        success:function(data){
			console.log(data.shortened_link);
			$('#url').val(window.location+data.shortened_link);
			$("#shortenButton").css("display", "none");
			$("#copyButton").css("display", "block");

        },
        error : function(xhr,errmsg,err) {
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
    });
});