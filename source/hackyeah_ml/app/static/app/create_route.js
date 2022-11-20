function initMap() {
  var directionsService = new google.maps.DirectionsService();
  var directionsRenderer = new google.maps.DirectionsRenderer();
  var chicago = new google.maps.LatLng(41.850033, -87.6500523);
  var mapOptions = {
    zoom:7,
    center: chicago
  }
  var map = new google.maps.Map(document.getElementById('map'), mapOptions);
  directionsRenderer.setMap(map);

  fetch('/app/maps')
  .then(res => res.json())
  .then(data => {
    var request = {
      origin: data.start,
      destination: data.end,
      waypoints: data.waypoints.map(wp => ({location: wp})),
      travelMode: 'DRIVING'
    };
  
    directionsService.route(request, function(result, status) {
      if (status == 'OK') {
        directionsRenderer.setDirections(result);
      }
    });
  })

}

window.initMap = initMap;