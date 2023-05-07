```
usage: json2csv [-h] [--input-data-base [IN_BASE]]
                [--output-delimiter [OUT_DELIMITER]]
                input

------------------------------------------------------------------------------
Convert JSON input file into CSV output file. If have nested values,
the output will contatenate the names with "."

------------------------------------------------------------------------------

positional arguments:
  input                 path to JSON file on disk. Use - for stdin

options:
  -h, --help            show this help message and exit
  --input-data-base [IN_BASE]
                        In case input data already is not a array of
                        objects/list, this allow explicitly inform the base.
                        Often is 'data'.
  --output-delimiter [OUT_DELIMITER]
                        The input delimiter

------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------

    json2csv --help

    json2csv input.json > output.csv

------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------

```