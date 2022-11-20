// Initialize and add the map
function calcRoute() {
  var directionsService = new google.maps.DirectionsService();
  var directionsRenderer = new google.maps.DirectionsRenderer();
  var krakow = new google.maps.LatLng(50.063463, 19.946079);
  var mapOptions = {
    zoom:7,
    center: krakow
  }
  var map = new google.maps.Map(document.getElementById('map'), mapOptions);
  directionsRenderer.setMap(map);
  directionsRenderer.setPanel(document.getElementById('directionsPanel'));
  fetch('http://127.0.0.1:8080/app/generate_route_google_api_url/plastic', {
    method: 'GET'
  })
 .then(response => response.json())
 .then(text => {
    directionsRenderer.setDirections(text)
 })

//    directionsService.route(''), function(response, status) {
//    if (status == 'OK') {

//    } else {
//      console.log(status)
//    }
//  });
}

window.initMap = calcRoute;