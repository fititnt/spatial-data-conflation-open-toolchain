```
usage: geojsonconcat [-h] [--format-output [{RFC7946,RFC8142}]]
                     inputs [inputs ...]

------------------------------------------------------------------------------
Concat 2 or more GeoJSON files into GeoJSON (RFC 7946) or
GeoJSON Text Sequences (RFC 8142)

@TODO for input files know to be GeoJSONSeq, read line by line

------------------------------------------------------------------------------

positional arguments:
  inputs                One or more input GeoJSON/GeoJSONSeq

options:
  -h, --help            show this help message and exit
  --format-output [{RFC7946,RFC8142}]
                        Output format GeoJSON (RFC7946) or GeoJSON Text
                        Sequences (RFC 8142)

------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
    geojsonconcat --help

    geojsonconcat input-a.geojson input-b.geojson > merged-a+b.geojson

    geojsonconcat --format-output=RFC8142 input-a.geojson input-b.geojson > merged-a+b.geojsonseq

------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------

```