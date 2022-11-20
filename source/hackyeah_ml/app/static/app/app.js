// Initialize and add the map
function initMap() {

    // The location of Krakow
    const krakow = { lat: 50.060, lng: 19.948 };
    const mama = { lat: 50.066, lng: 19.950 };
    // The map, centered at Krakow
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 12,
      center: krakow,
    });
    // The marker, positioned at Krakow
    const marker = new google.maps.Marker({
      position: krakow,
      map: map,
    });
    // The marker, positioned at Krakow
    const marker2 = new google.maps.Marker({
        position: mama,
        map: map,
        });

  }
  
  window.initMap = initMap;

  