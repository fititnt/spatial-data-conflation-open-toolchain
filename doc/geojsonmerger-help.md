```
usage: geojsonmerger [-h] [--format-output [{auto,geojson,geojsonseq}]]
                     [--rename-attribute [RENAME_ATTR]]
                     [--value-fixed [VALUE_FIXED]]
                     [--value-norm-name-place [VALUE_NAME_PLACE]]
                     geodataset_a geodataset_b

------------------------------------------------------------------------------
[DRAFT] GeoJSON simple merger

Merge extra attributes from an GeoJSON (likely the one with more metadata, but
not accurate geometry) into another GeoJSON.

------------------------------------------------------------------------------

positional arguments:
  geodataset_a          GeoJSON dataset 'A'
  geodataset_b          GeoJSON dataset 'B'

options:
  -h, --help            show this help message and exit
  --format-output [{auto,geojson,geojsonseq}]
                        Path to output file

Change properties from each item:
  --rename-attribute [RENAME_ATTR]
                        Rename attribute (if exist). Use '||' to divide the
                        source key and target key. Accept multiple values.
                        Example: --rename-attribute='NAME|||name' --rename-
                        attribute='CITY|||addr:city'
  --value-fixed [VALUE_FIXED]
                        Define a fixed string for every value of a column, For
                        multiple, use multiple times this parameter. Source vs
                        destiny column must be divided by |||. Example: <[
                        --value-fixed='source|||BR:DATASUS' ]>
  --value-norm-name-place [VALUE_NAME_PLACE]
                        Column to normalize value (strategy: name of place).
                        Accept multiple options. Example: --value-norm-name-
                        place='name' --value-norm-name-place='alt_name'

------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
    geojsonmerger --help

------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------

```