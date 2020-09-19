$(document).ready(function() {

  $("#searchbutton").click( function(e) {
      displayModal();
  })

  $("#searchfield").keydown( function (e) {
      if(e.keyCode == 13) {
        displayModal();
      }	
  });

  function displayModal() {
      $("#myModal").modal('show');
  
      $("#status").html("Buscando...");
      $("#previous").hide();
      $("#next").hide();
      $.getJSON(`/search/${$("#searchfield").val()}` , function(data) {
        renderQueryResults(data);
      });
  }

  $("#next").click( function(e) {
      //@TODO
  });
  
  $("#previous").click( function(e) {
      //@TODO
  });

  function renderQueryResults(data) {
  
    if (data.error != undefined) {
      $("#status").html("Error: "+data.error);
    } else {
      $("#status").html(""+data.num_results+" result(s)");

      //Aqui insertamos el codigo para desplegar las imagenes.
      
      $("#previous").show();  
      $("#next").show();          
    }
  }
 
})



