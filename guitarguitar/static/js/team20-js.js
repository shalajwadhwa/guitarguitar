$(document).ready(function() {
	$(document).on("click", ".chat-button", function() {
		var text = encodeURI($('.querybox').val()); // get query from textbox
		$('.querybox').attr("placeholder", "🤔...")
		$(".chat-container-card").append("<div class=\"row mt-3\">\
		    <div class=\"col-6 offset-6\">\
		        <div class=\"card w-100 query-bubble\">\
		            <p class=\"card-text query-text\">" + decodeURI(text) + "</p>\
		        </div>\
		    </div>\
		</div>\
		<div class=\"row mt-3\">"); // append the user's query to the chat log container
		$('.querybox').val(""); // clear input box
		window.scrollTo(0, document.body.scrollHeight);
		$.get('/team20/answer/',
			  {'query': text},
		      function(data) {
		        	$(".chat-container-card").append(data);
		        	window.scrollTo(0, document.body.scrollHeight);
		        	$('.querybox').attr("placeholder", "What would you like to say?")
		      }) // send query and append the response element returned back from the backend, then scroll to bottom
    });
	$('.querybox').keypress(function(e) {
	 	var key = e.which;
	 	if(key == 13) {
	    	$(".chat-button").click();
	  	}
	});
});