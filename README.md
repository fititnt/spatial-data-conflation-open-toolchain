# spatial-data-conflation-open-toolchain
[![GitHub](https://img.shields.io/badge/GitHub-fititnt%20spatial--data--conflation--open--toolchain-lightgrey?logo=github&style=social[fititnt/geojson-diff] "GitHub")](https://github.com/fititnt/spatial-data-conflation-open-toolchain)
[![Pypi: gis-conflation-toolchain](https://img.shields.io/badge/python%20pypi-gis--conflation--toolchain-brightgreen[Python] 
 "Pypi: gis-conflation-toolchain")](https://pypi.org/project/gis-conflation-toolchain)

**[EARLY DRAFT] Open, free to use, toolchain for geospatial data conflation. Command-line interface for file manipulation.** _See geojson-diff.py from <https://github.com/fititnt/openstreetmap-vs-dados-abertos-brasil>._

## Installing

```bash
pip install --upgrade gis-conflation-toolchain
```

<!--
-  Saalfield, Alan. Conflation: Automated Map Compilation. BUREAU OF THE CENSUS STATISTICAL RESEARCH DIVISION REPORT SERIES, SRD Research Report Number: Census/SRD/RR-87124
  - https://www.census.gov/content/dam/Census/library/working-papers/1987/adrm/rr87-24.pdf
- Lynch, M. and A. Saalfeld, 1985, "Conflation: Automated Map Compilation, a Video Game Approach", Proceedings, Auto-Carto VII
  - https://cartogis.org/docs/proceedings/archive/auto-carto-7/pdf/conflation-automated-map-compilation-a-video-game-approach.pdf
-->

## Toolchain

<!--
Rebuld documentation with
    ./generate-help-markdown.sh
-->

### csv2excel
- [doc/csv2excel-help.md](doc/csv2excel-help.md)

### csvedit
- [doc/csvedit-help.md](doc/csvedit-help.md)

### dictionarybuilder
- [doc/dictionarybuilder-help.md](doc/dictionarybuilder-help.md)

### geojsondiff
- [doc/geojsondiff-help.md](doc/geojsondiff-help.md)

### geojsonconcat
- [doc/geojsonconcat-help.md](doc/geojsonconcat-help.md)

### geojsonedit
- [doc/geojsonedit-help.md](doc/geojsonedit-help.md)

### geojsonmerger
- [doc/geojsonmerger-help.md](doc/geojsonmerger-help.md)

### csv2geojson
- [doc/csv2geojson-help.md](doc/csv2geojson-help.md)

### json2csv
- [doc/json2csv-help.md](doc/json2csv-help.md)

### overpassql2osmf
- [doc/overpassql2osmf-help.md](doc/overpassql2osmf-help.md)

<!--

osmf2geojson
osmf2geojson tests/data/test2.osm

# https://docs.osmcode.org/osmium/latest/osmium-sort.html
osmium sort -o tests/data/test2-v2.osm tests/data/test2.osm
osmium sort -o tests/data/test1-v2.osm tests/data/test1.osm
osmf2geojson tests/data/test2-v2.osm > tests/temp/test2-v2.geojson
osmf2geojson tests/data/test1-v2.osm > tests/temp/test1-v2.geojson
-->
