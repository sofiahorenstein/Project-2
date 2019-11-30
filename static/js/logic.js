// Create our initial map object
// Set the longitude, latitude, and the starting zoom level
//var chosenState = objDropDown.value;
var myMap = L.map("map", {
  center: [40.1430058,-74.7311156],
  zoom: 8
});

// Add a tile layer 
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(myMap);


var select;
window.onload = function () {
    select = document.getElementById('dropdown');
    console.log(select);
}

function changeHiddenInput(objDropDown) {
    console.log(objDropDown);
    var objHidden = document.getElementById("hiddenInput");
    objHidden.value = objDropDown.value;
    var chosenState = objHidden.value;
    result.innerHTML = chosenState || "";
}

function clearMarkers(layerGroup) {
  layerGroup.clearLayers();
}

states = [ { "state" : "NY",
            "lat" : 42.62,
            "lon" : -73.83,
            "zoom" : 7},
            {"state" : "NJ",
            "lat" : 40.1430058,
            "lon" : -74.7311156,
            "zoom": 8},
            {"state" : "CT",
            "lat" : 41.5187835,
            "lon" : -72.757507,
            "zoom" : 9}];

// Add the markers
function selectState(objDropDown) {
  
  var objHidden = document.getElementById("hiddenInput");
  objHidden.value = objDropDown.value;
  var chosenState = objHidden.value;
  for (var j = 0; j < states.length; j++) {
    if (states[j].state === chosenState){
      var stateLat = states[j].lat;
      var stateLon = states[j].lon;
      var zoom = states[j].zoom;
      myMap.flyTo([stateLat, stateLon], zoom);
    }
  }
  
  for (var i = 0; i < data.length; i++) {

    if (data[i].state === chosenState){
      var lat = parseFloat(data[i].latitude);
      var long = parseFloat(data[i].longitude);
      var lon = long - (long * 2);
      var state = data[i].state
      console.log(lat, lon, state);
      var list = "<dl>"
           + "<dd>" + data[i].name + "</dd>"
           + "<dd>" + data[i].address1 + "</dd>" 
           + "<dd>" + data[i].city + " " + data[i].state + "</dd>"
           + "<dd>" + data[i].email + " " + data[i].phone + "</dd>" 
           + "</d1>";
      var layerGroup = L.clearLayers().layerGroup().addTo(myMap);
      var marker = L.marker([lat, -lon]).addTo(layerGroup);
      marker.bindPopup(list);
    }
  };
  
}



