// Create our initial map object
// Set the longitude, latitude, and the starting zoom level
var myMap = L.map("map", {
  center: [39, -95],
  zoom: 4
});

// Add a tile layer 
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(myMap);


// Add the markers
for (var i = 0; i < data.length; i++) {
  var lat = parseFloat(data[i].latitude);
  var long = parseFloat(data[i].longitude);
  var lon = long - (long * 2);
  //console.log(lat, lon);
  var list = "<dl>"
           + "<dd>" + data[i].name + "</dd>"
           + "<dd>" + data[i].address1 + "</dd>" 
           + "<dd>" + data[i].city + " " + data[i].state + "</dd>"
           + "<dd>" + data[i].email + " " + data[i].phone + "</dd>" 
           + "</d1>";
           
  
  var marker = L.marker([lat, -lon]).addTo(myMap);
  marker.bindPopup(list);
};