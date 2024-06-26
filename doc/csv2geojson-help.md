```
usage: csv2geojson [-h] [--lat [LAT]] [--lon [LON]]
                   [--lat-lon-empty [NO_LATLON]]
                   [--filter-contain [FILTER_CONTAIN]]
                   [--filter-contain-regex [FILTER_CONTAIN_REGEX]]
                   [--contain-or [CONTAIN_OR]] [--contain-and [CONTAIN_AND]]
                   [--contain-and-in [CONTAIN_AND_IN]]
                   [--delimiter [DELIMITER]] [--encoding [ENCODING]]
                   [--output-type [{GeoJSON,GeoJSONSeq}]] [--ignore-warnings]
                   [--cast-integer [CAST_INTEGER]] [--cast-float [CAST_FLOAT]]
                   [--column-copy-to [COLUMN_COPY]]
                   [--value-fixed [VALUE_FIXED]]
                   [--value-prepend [VALUE_PREPEND]]
                   [--value-postcode-br [VALUE_POSTCODE_BR]]
                   [--value-phone-br [VALUE_PHONE_BR]]
                   [--value-name-place-br [VALUE_NAME_PLACE_BR]]
                   [--value-name-street-br [VALUE_NAME_STREET_BR]]
                   [--output-know-fields [OUTPUT_FIELDS_KNOW]]
                   [--output-unknow-action {_prepend,discard}]
                   [--output-delete-fields [OUTPUT_DELETE_FIELDS]]
                   [--output-nohousenumber-values [OUTPUT_NOHOUSENUMBER_VALUES]]
                   [--output-sort-keys]
                   [--preprocessor-item-custom-inep [PREPITEM_CUSTOM_INEP]]
                   [--preprocessor-complex-cnefe [PREP_COMPLEX_CNEFE]]
                   input

------------------------------------------------------------------------------
CSV to GeoJSON

------------------------------------------------------------------------------

positional arguments:
  input                 path to CSV file on disk. Use - for stdin

options:
  -h, --help            show this help message and exit
  --lat [LAT]           the name of the latitude column
  --lon [LON]           the name of the longitude column
  --lat-lon-empty [NO_LATLON]
                        Disable copy a latitude langitude and create am Point
                        on 0, 0
  --filter-contain [FILTER_CONTAIN]
                        Filter one or more fields for contain a stringUse
                        '|||' to divide the field and the string. Accept
                        multiple values. Example: --filter-
                        contain='name|||hospital'
  --filter-contain-regex [FILTER_CONTAIN_REGEX]
                        If defined, only results that match all clauses will
                        appear on output. Accept multiple values.Syntax is
                        python regex.
                        https://docs.python.org/3/library/re.htmlExample:
                        --filter-contain-regex='name|||hospital.+'
  --contain-or [CONTAIN_OR]
                        If defined, only results that match at least one
                        clause will appear on output. Accept multiple values.
                        --contain-or=tag1=value1 --contain-or=tag2=value2
  --contain-and [CONTAIN_AND]
                        If defined, only results that match all clauses will
                        appear on output. Accept multiple values.--contain-
                        and=tag1=value1 --contain-and=tag2=value2
  --contain-and-in [CONTAIN_AND_IN]
                        Alternative to -contain-and where values for a single
                        field are a list. Separe values with ||Accept multiple
                        values.--contain-and=tag_a=valuea1||valuea2||valuea3
  --delimiter [DELIMITER]
                        the type of delimiter
  --encoding [ENCODING]
                        the type of delimiter
  --output-type [{GeoJSON,GeoJSONSeq}]
                        Change the default output type.See https://www.rfc-
                        editor.org/rfc/rfc8142 and
                        https://stevage.github.io/ndgeojson/
  --ignore-warnings     Ignore some errors (such as empty latitude/longitude
                        values)

Convert/preprocess data from input, including generate new fields:
  --cast-integer [CAST_INTEGER]
                        Name of input fields to cast to integer. Use | for
                        multiple. Example: <[ --cast-
                        integer='field_a|field_b|field_c' ]>
  --cast-float [CAST_FLOAT]
                        Name of input fields to cast to float. Use | for
                        multiple. Example: <[ --cast-
                        float='latitude|longitude|field_c' ]>
  --column-copy-to [COLUMN_COPY]
                        Add extra comluns. For multiple, use multiple times
                        this parameter. Source vs destiny column must be
                        divided by |. Example: <[ --column-copy-
                        to='ORIGINAL_FIELD_PT|name:pt' --column-copy-
                        to='CNPJ|ref:vatin' ]>
  --value-fixed [VALUE_FIXED]
                        Define a fixed string for every value of a column, For
                        multiple, use multiple times this parameter. Source vs
                        destiny column must be divided by |. Example: <[
                        --value-fixed='source|BR:DATASUS' ]>
  --value-prepend [VALUE_PREPEND]
                        Prepend a custom string to all values in a column. For
                        multiple, use multiple times this parameter. Source vs
                        destiny column must be divided by |. Example: <[
                        --value-prepend='ref:vatin|BR' ]>
  --value-postcode-br [VALUE_POSTCODE_BR]
                        One or more column names to format as if was Brazilan
                        postcodes, CEP
  --value-phone-br [VALUE_PHONE_BR]
                        One or more column names to format as Brazilian
                        phone/fax/WhatsApp number
  --value-name-place-br [VALUE_NAME_PLACE_BR]
                        One or more columsn to format as name of place (Locale
                        BR)
  --value-name-street-br [VALUE_NAME_STREET_BR]
                        One or more columsn to format as name of street
                        (Locale BR, 'logradouro')

Post Processing (mostly how to deal with unknow fields):
  --output-know-fields [OUTPUT_FIELDS_KNOW]
                        List of of know fields (ones no further process is
                        need).Necessary to allow inform what to do with unknow
                        fields. Divide with |. Example:
                        'name|addr:housenumber:addr:street'
  --output-unknow-action {_prepend,discard}
                        What to do with unknow fields. Requires --output-know-
                        fields
  --output-delete-fields [OUTPUT_DELETE_FIELDS]
                        Fields that (if exist) always delete from output.
                        Split by |
  --output-nohousenumber-values [OUTPUT_NOHOUSENUMBER_VALUES]
                        Which values on addr:housenumber replace it by
                        nohousenumber=yes. Split by | .Examples:
                        'N/A|n/a|na|S/N|s/n|sn'
  --output-sort-keys    Sort keys

Other:
  --preprocessor-item-custom-inep [PREPITEM_CUSTOM_INEP]
                        Custom feature not yet documented
  --preprocessor-complex-cnefe [PREP_COMPLEX_CNEFE]
                        Preprocessor for IBGE CNEFE 20221: full metadata; 0:
                        code-only; -1: no codes; -999: debug minimal

------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
File on disk . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

    csv2geojson --lat=NU_LATITUDE --lon=NU_LONGITUDE --delimiter=';' --encoding='latin-1' data/tmp/DATASUS-tbEstabelecimento.csv

STDIN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
(Note the "-" at the end)
    head data/tmp/DATASUS-tbEstabelecimento.csv | csv2geojson --lat=NU_LATITUDE --lon=NU_LONGITUDE --delimiter=';' --encoding='latin-1' -

(With jq to format output)
    head data/tmp/DATASUS-tbEstabelecimento.csv | csv2geojson --lat=NU_LATITUDE --lon=NU_LONGITUDE --delimiter=';' --encoding='latin-1' --ignore-warnings - | jq

GeoJSONL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    echo "See https://stevage.github.io/ndgeojson/"
    echo "same as GeoJSONSeq"

GeoJSONSeq . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    head data/tmp/DATASUS-tbEstabelecimento.csv | csv2geojson --lat=NU_LATITUDE --lon=NU_LONGITUDE --delimiter=';' --encoding='latin-1' --output-type=GeoJSONSeq --ignore-warnings -

    head data/tmp/DATASUS-tbEstabelecimento.csv | csv2geojson --lat=NU_LATITUDE --lon=NU_LONGITUDE --delimiter=';' --encoding='latin-1' --output-type=GeoJSONSeq --ignore-warnings - > data/tmp/DATASUS-tbEstabelecimento-head.geojsonl

GeoJSONSec -> Geopackage . . . . . . . . . . . . . . . . . . . . . . . . . . .
    csv2geojson --lat=NU_LATITUDE --lon=NU_LONGITUDE --delimiter=';' --encoding='latin-1' --output-type=GeoJSONSeq --ignore-warnings data/tmp/DATASUS-tbEstabelecimento.csv > data/tmp/DATASUS-tbEstabelecimento.geojsonl

    ogr2ogr -f GPKG data/tmp/DATASUS-tbEstabelecimento.gpkg data/tmp/DATASUS-tbEstabelecimento.geojsonl

Exemplo CNPJ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
(https://www.gov.br/receitafederal/dados/cnpj-metadados.pdf)
CNPJ_BASICO;CNPJ_ORDEM;CNPJ_DV;IDENTIFICADOR;MATRIZ_FILIAL;SITUAÇÃO_CADASTRAL;DATA_SITUACAO_CADASTRAL;MOTIVO_SITUACAO_CADASTRAL;NOME_DA_CIDADE_NO_EXTERIOR;PAIS;DATA_DE_INICIO_ATIVIDADE;CNAE_FISCAL_PRINCIPAL;CNAE_FISCAL_SECUNDÁRIA;TIPO_DE_LOGRADOURO;LOGRADOURO;NUMERO;COMPLEMENTO;BAIRRO;CEP;UF;MUNICIPIO;DDD_1;TELEFONE_1;DDD_2;TELEFONE_2;DDD_DO_FAX;FAX;CORREIO_ELETRONICO;SITUACAO_ESPECIAL;DATA_DA_SITUACAO_ESPECIAL
------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------

```