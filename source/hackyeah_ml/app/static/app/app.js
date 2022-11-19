// Initialize and add the map
function initMap() {
    // The location of Uluru
    const krakow = { lat: 50.064, lng: 19.945 };
    // The map, centered at Uluru
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 12,
      center: krakow,
    });
    // The marker, positioned at Krakow
    const marker = new google.maps.Marker({
      position: krakow,
      map: map,
    });
  }
  
  window.initMap = initMap;