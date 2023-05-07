```
usage: dictionarybuilder [-h] [--input-delimiter [IN_DELIMITER]]
                         [--input-encoding [IN_ENCODING]]
                         [--input-fieldnames [IN_FIELDNAMES]]
                         [--dict-target-key [DICT_TARGET]]
                         [--dict-source-key [DICT_SOURCES]]
                         input

------------------------------------------------------------------------------
Convert 2 or more columns of one CSV input file into a dictionary (a sorted
2 column RS delimited file) optimized to be used by other tools as simple
pivot file to replace or append new values to existing datasets

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
  --dict-target-key [DICT_TARGET]
                        Field name to represent the primary key to convert
                        data Defaults to first column. Example: --dict-target-
                        key='id'
  --dict-source-key [DICT_SOURCES]
                        Field name to be used as source to convert data to
                        target key. If undefined, defaults to all fields which
                        are not the --dict-target-key. Example: --dict-source-
                        key='name' --dict-source-key='title'

------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------

    dictionarybuilder --help

------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------

```