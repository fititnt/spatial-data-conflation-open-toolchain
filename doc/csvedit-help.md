```
usage: csvedit [-h] [--input-delimiter [IN_DELIMITER]]
               [--input-encoding [IN_ENCODING]]
               [--input-fieldnames [IN_FIELDNAMES]]
               [--output-delimiter [OUT_DELIMITER]]
               input

------------------------------------------------------------------------------
CSV simple editor

------------------------------------------------------------------------------

positional arguments:
  input                 path to CSV file on disk. Use - for stdin

options:
  -h, --help            show this help message and exit
  --input-delimiter [IN_DELIMITER]
                        The input delimiter
  --input-encoding [IN_ENCODING]
                        The input encoding
  --input-fieldnames [IN_FIELDNAMES]
                        If the input CSV does not have a header, specify here.
                        Use | as separator (if a field de de facto have |,
                        then use \|). Example: --input-fieldnames='field with
                        \| on it|another field'
  --output-delimiter [OUT_DELIMITER]
                        The output delimiter

------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------

    csvedit --help

------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------

```