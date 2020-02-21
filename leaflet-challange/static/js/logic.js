    var url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson";

    d3.json(url,function(data){
    function CircleMarker(feature,latlng){
        let options = {
            radius:feature.properties.mag*4,
            fillColor: chooseColor(feature.properties.mag),
            color: "black",
            weight: 1,
            opacity: 1,
            fillOpacity: 0.6
        }
        return L.circleMarker( latlng, options );
    }


    var earthQuakes = L.geoJSON(data,{
        onEachFeature: function(feature,layer){
            layer.bindPopup("Place:"+feature.properties.place + "<br> Mag: "+feature.properties.mag+"<br> Date: "+new Date(feature.properties.time));
        },
        pointToLayer: CircleMarker

    });

    createMap(earthQuakes);

    });

  function createMap(earthQuakes) {

    
    var satellite = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
      attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
      maxZoom: 18,
      id: "mapbox.satellite",
      accessToken: API_KEY
    });
  
    var grayscale = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
      attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
      maxZoom: 18,
      id: "mapbox.light",
      accessToken: API_KEY
    });

    var outdoors = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
      attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
      maxZoom: 18,
      id: "mapbox.outdoors",
      accessToken: API_KEY
    });

    var dark = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox.dark',
        accessToken: API_KEY
    });
  
    var baseMaps = {
      "Satellite": satellite,
      "Grayscale": grayscale,
      "Outdoors": outdoors,
      "Dark": dark
    };
  
    var myMap = L.map("map", {
      center: [
        37.0902405,-95.7128906
      ],
      zoom: 4,
      layers: [satellite, earthQuakes]
    });
  }


  function Color(mag){
    if (mag < 1) {
        return "red";}

        else if (mag < 2){
            return "blue";}
            
        else if (mag < 3){
            return "yellow";}

        else if (mag < 4){
            return "purple";}
                
        else if (mag < 5){
            return "orange";}
                    
        else {
            return "green";}
    };
}
