$(document).ready(function() {              // attach a handler to an event for the elements



    $(".whiteTextOnHover").mouseover(function(){
      $(this).css("color", "white");
    });
    $(".whiteTextOnHover").mouseout(function(){
      $(this).css("color", "black");
    });

});