//[out:json][timeout:25];
[out:xml][timeout:25];
// {{geocodeArea:Rio Grande do Sul}}->.searchArea;
area(id:3600242620)->.searchArea;
(
  nwr["ref:CNES"](area.searchArea);
  nwr["healthcare"="hospital"](area.searchArea);
  nwr["amenity"="hospital"](area.searchArea);
  //nwr["amenity"="clinic"](area.searchArea);
  //nwr["amenity"="social_facility"](area.searchArea);
  //nwr["amenity"="pharmacy"](area.searchArea);
  //nwr["amenity"="doctors"](area.searchArea);
);
out body;
>;
out skel qt;
