
let counter = 0;
let stepOfFour = 4;
let list_urls = []

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
      if ((counter+4) < list_urls.length) {
          counter += 4;
          renderWithList()
      }
  });
  
  $("#previous").click( function(e) {
      //@TODO
       if ((counter-4) >= 0) {
          counter -= 4;
          renderWithList()
      }
  });

  function renderQueryResults(data) {
  
    if (data.error != undefined) {
      $("#status").html("Error: "+data.error);
    } else {
      $("#status").html(""+data.num_results+" result(s)");

      console.log(data)
      list_urls = data.results;
        renderWithList();

      //Aqui insertamos el codigo para desplegar las imagenes.
      
      $("#previous").show();  
      $("#next").show();          
    }
  }
 
})

function renderWithList() {
     $("#photo1").html(`<img src="${list_urls[counter]}" alt="image" 
        style="display: table-cell; vertical-align: inherit; width:100px; height:100px;">`);
      $("#photo2").html(`<img src="${list_urls[counter+1]}" alt="image" 
        style="display: table-cell; vertical-align: inherit; width:100px; height:100px;">`);
      $("#photo3").html(`<img src="${list_urls[counter+2]}" alt="image" 
        style="display: table-cell; vertical-align: inherit; width:100px; height:100px;">`);
      $("#photo4").html(`<img src="${list_urls[counter+3]}" alt="image" 
        style="display: table-cell; vertical-align: inherit; width:100px; height:100px;">`);
}



