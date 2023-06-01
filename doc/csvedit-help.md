```
usage: csvedit [-h] [--input-delimiter [IN_DELIMITER]]
               [--input-encoding [IN_ENCODING]]
               [--input-fieldnames [IN_FIELDNAMES]]
               [--output-delimiter [OUT_DELIMITER]]
               [--contain-and [CONTAIN_AND]]
               [--filter-contain [FILTER_CONTAIN]]
               input

------------------------------------------------------------------------------
CSV simple command line editor

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

Filter rows:
  --contain-and [CONTAIN_AND]
                        If defined, only results that match all clauses will
                        appear on output. Accept multiple values.--contain-
                        and=tag1=value1 --contain-and=tag2=value2
  --filter-contain [FILTER_CONTAIN]
                        Filter one or more fields for contain a stringUse
                        '|||' to divide the field and the string. Accept
                        multiple values. Example: --filter-
                        contain='name|||hospital'

------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------

    csvedit --help

------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------

```