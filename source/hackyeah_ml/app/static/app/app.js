//buttons handler

const btn_submit = document.querySelector('#option_submit');        
const radioButtons = document.querySelectorAll('input[name="options"]');

btn_submit.addEventListener("click", () => {
    
    let selectedWaste;
    for (const radioButton of radioButtons) {
        if (radioButton.checked) {
            selectedWaste = radioButton.value;
            break;
        }
    }

    console.log(`click! ${selectedWaste}`)
});

//Get the data

class MarkerGenerator {
    constructor(barWidth, barSpacing, maxHeight) {
      this.barWidth = barWidth;
      this.barSpacing = barSpacing;
      this.maxHeight = maxHeight;
    }
    
    generate(markersData) {
      let markers = [];
      markersData.forEach((markerData, index) => {
        markers.push({
          path: `M${index * (this.barWidth + this.barSpacing)},${this.maxHeight} l${this.barWidth},0 l0,-${Math.round(markerData.value * this.maxHeight)} l-${this.barWidth},0 Z`,
          fillColor: markerData.color,
          fillOpacity: 1,
          strokeWeight: 0,
          rotation: 0,
          scale: 1,
          anchor: new google.maps.Point(15, 30),
        })
      });
      return markers;
    }
  }
  
  const g = new MarkerGenerator(5, 2, 50);

var allMarkers = {}


// Initialize and add the map
function initMap() {

    // The location of waste facilities and containers
    const pointers_hub = { lat: 50.060, lng: 19.948 }
     // The map, centered at Krakow
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 12,
      center: pointers_hub,
    });

    setInterval(() => {
        fetch('/app/weight')
    .then(response => response.json())
    .then(data => {

        let pointers = Object.values(data)
        pointers[0].lat = 50.069063155047395
        pointers[0].long = 19.990572280177357
        pointers[0].weights[0].weight *= 500
        pointers[0].weights[1].weight *= 500
        console.log(pointers)

        const typeColorMap = {
            mix: 'black',
            plastic: 'yellow',
            bio: 'brown',
            paper: 'green',
            glass: 'blue'
        }

        pointers.forEach((pointer, pi) => {
            if(allMarkers[pi] == undefined) {
                allMarkers[pi] = []
            }

            //pointer.weights.filter()
            //console.log(pointer.weights[0].type)
            pointer.weights = pointer.weights.sort((scale1, scale2) => scale1.type > scale2.type ? -1:1)
            let markersData = pointer.weights.map(scale => ({color: typeColorMap[scale.type], value: scale.weight/1500}))

            markersData = g.generate(markersData)

            markersData.forEach((markerData, mi) => {
                if (allMarkers[pi].length != markersData.length) {
                    allMarkers[pi].push(new google.maps.Marker({
                        position: new google.maps.LatLng(pointer.lat, pointer.long),
                        icon: markerData,
                        map: map,
                    }))
                } else {
                    allMarkers[pi][mi].setIcon(markerData)
                }
            })

        }) 
    })
    }, 500)


  }
  
  window.initMap = initMap;


  