```
usage: overpassql2osmf [-h] input_query

------------------------------------------------------------------------------
overpassql2osmf v0.2.0 convert Overpass Query Language to am OSM File (XML)

------------------------------------------------------------------------------

positional arguments:
  input_query  Input OverpassQL query or path to .overpassql file

options:
  -h, --help   show this help message and exit

------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
Input file contains Overpass query . . . . . . . . . . . . . . . . . . . . . .
    overpassql2osmf tests/data/cnes.overpassql > tests/temp/cnes.osm

CSV Output (requires special Overpass query) . . . . . . . . . . . . . . . . .

    overpassql2osmf '[out:csv(::id,::type,"name")]; area[name="Bonn"]; nwr(area)[railway=station]; out;' > tests/temp/bonn.osm.csv
------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------

```