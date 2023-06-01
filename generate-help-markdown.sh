#!/bin/bash

# run with
#    ./generate-help-markdown.sh

# csv2gecodedcsv: not ready for now

printf '```\n' > doc/csv2excel-help.md
csv2excel --help >> doc/csv2excel-help.md
printf '\n```' >> doc/csv2excel-help.md

printf '```\n' > doc/csvedit-help.md
csvedit --help >> doc/csvedit-help.md
printf '\n```' >> doc/csvedit-help.md

printf '```\n' > doc/dictionarybuilder-help.md
dictionarybuilder --help >> doc/dictionarybuilder-help.md
printf '\n```' >> doc/dictionarybuilder-help.md

printf '```\n' > doc/geojsonconcat-help.md
geojsonconcat --help >> doc/geojsonconcat-help.md
printf '\n```' >> doc/geojsonconcat-help.md

printf '```\n' > doc/geojsondiff-help.md
geojsondiff --help >> doc/geojsondiff-help.md
printf '\n```' >> doc/geojsondiff-help.md

printf '```\n' > doc/geojsonedit-help.md
geojsonedit --help >> doc/geojsonedit-help.md
printf '\n```' >> doc/geojsonedit-help.md

printf '```\n' > doc/geojsonmerger-help.md
geojsonmerger --help >> doc/geojsonmerger-help.md
printf '\n```' >> doc/geojsonmerger-help.md

printf '```\n' > doc/csv2geojson-help.md
csv2geojson --help >> doc/csv2geojson-help.md
printf '\n```' >> doc/csv2geojson-help.md

printf '```\n' > doc/json2csv-help.md
json2csv --help >> doc/json2csv-help.md
printf '\n```' >> doc/json2csv-help.md

# osmf2geojson: please just use osmium cli tools directly

printf '```\n' > doc/overpassql2osmf-help.md
overpassql2osmf --help >> doc/overpassql2osmf-help.md
printf '\n```' >> doc/overpassql2osmf-help.md


# csv2excel --help > doc/csv2excel-help.md
# csv2geojson --help > doc/csv2geojson-help.md
# overpassql2osmf --help > doc/overpassql2osmf-help.md