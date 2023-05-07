```
usage: geojsonedit [-h] [--format-output [{auto,geojson,geojsonseq}]]
                   [--rename-attribute [RENAME_ATTR]]
                   [--value-fixed [VALUE_FIXED]]
                   [--value-norm-name-place [VALUE_NAME_PLACE]]
                   input

------------------------------------------------------------------------------
GeoJSON / GeoJSONSeq command line editor

------------------------------------------------------------------------------

positional arguments:
  input                 Input GeoJSON / GeoJSONSeq. Use - for stdin

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
    geojsonedit --help

------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------

```