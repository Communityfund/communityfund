$(document).read(function() {

  //Let the user know their login information is not valid. 
  function handle_error() {
    document.getElementById("message").innerHTML = "That's not a valid username/password combination.";
    $("#errorMessage").css('visibility','visible').hide().fadeIn(500);
    setTimeout(function() {$("#errorMessage").fadeOut(500);}, 2000);
  }

  //Submit login form using AJAX. 
  $("#login-form").submit(function() {  
    $.ajax({
      data: $(this).serialize(),
      type: $(this).attr('method'),
      url: $(this).attr('action'),
      success: function(response) {

      },
      error: function(e, x, r) {
        handle_error();
      }
    });
    return false;
  });
});



