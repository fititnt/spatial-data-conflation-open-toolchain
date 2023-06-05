```
usage: geojsondiff [-h] [--output-diff-geojson [OUTDIFFGEO]]
                   [--output-diff-csv [OUTDIFFCSV]]
                   [--output-diff-tsv [OUTDIFFTSV]] [--output-log [OUTLOG]]
                   [--conflation-strategy [{distance,addr}]]
                   [--tolerate-distance [TDIST]]
                   [--pivot-key-main [PIVOT_KEY_MAIN]]
                   [--pivot-attr-2 [PIVOT_ATTR_2]]
                   [--pivot-alias [PIVOT_ALIAS]]
                   [--prefilter-a-contain [PREFILTER_A_CONTAIN]]
                   [--prefilter-b-contain [PREFILTER_B_CONTAIN]]
                   [--filter-ab-dist-min [FILTER_AB_DIST_MIN]]
                   [--filter-ab-dist-max] [--filter-matched-pivot-key]
                   [--filter-matched-pivot-key-not]
                   [--output-josm-file [OUTOSC]]
                   geodataset_a geodataset_b

------------------------------------------------------------------------------
GeoJSON++ diff v0.6.2

------------------------------------------------------------------------------

positional arguments:
  geodataset_a          GeoJSON dataset 'A'
  geodataset_b          GeoJSON dataset 'B'

options:
  -h, --help            show this help message and exit
  --output-diff-geojson [OUTDIFFGEO]
                        (Experimental) Path to output GeoJSON diff file
  --output-diff-csv [OUTDIFFCSV]
                        Path to output CSV diff file
  --output-diff-tsv [OUTDIFFTSV]
                        Path to output TSV (Tab-separated values) diff file
  --output-log [OUTLOG]
                        Path to output file
  --conflation-strategy [{distance,addr}]
                        Conflation strategy.

Parameters used to know how to conflate A and B:
  --tolerate-distance [TDIST]
                        Typical maximum distance for features match if not
                        exact same point. In meters. Default to 100
  --pivot-key-main [PIVOT_KEY_MAIN]
                        If defined, its an strong hint that item from A and B
                        alredy are mached with each other. Use '||' if
                        attribute on A is not the same on the B. Accept
                        multiple values. Example: --pivot-key-
                        main='CO_CNES||ref:CNES' --pivot-key-main='ref:vatin'
  --pivot-attr-2 [PIVOT_ATTR_2]
                        A non primary attribute on A and B (like phone or
                        website) which while imperfect, is additional hint
                        about being about same. Use '||' if attribute on A is
                        not the same on the B. Accept multiple values.
                        Example: --pivot-attr-2='contact:email'
  --pivot-alias [PIVOT_ALIAS]
                        A weak (like name or description) attribute to order
                        the matches. Impefect. Never will return perfect
                        match, even if exact the same. Use '||' if attribute
                        on A is not the same on the B. Accept multiple values.
                        Example: --pivot-alias'COMPANY_NAME||name' --pivot-
                        alias'COMPANY_NAME||alt_name'

Pre-filter data before processing:
  --prefilter-a-contain [PREFILTER_A_CONTAIN]
                        Prefilter (e.g. before processing) a filed in A for a
                        stringUse '||' to divide the field and the string.
                        Accept multiple values. Example: --prefilter-a-
                        contain='NO_RAZAO_SOCIAL||hospital'
  --prefilter-b-contain [PREFILTER_B_CONTAIN]
                        Prefilter (e.g. before processing) a filed in B for a
                        stringUse '||' to divide the field and the string.
                        Accept multiple values. Example: --prefilter-a-
                        contain='name||hospital'

Quick output filters for GeoJSON output. Ignored by tabular diffs:
  --filter-ab-dist-min [FILTER_AB_DIST_MIN]
                        Minimal distance between A and B. Example: 0
  --filter-ab-dist-max  Minimal distance between A and B. Example: 0
  --filter-matched-pivot-key
                        Only output items matched by main pivot key
  --filter-matched-pivot-key-not
                        Do not output items matched by main pivot key

ADVANCED. Do not upload to OpenStreetMap unless you review the output. Requires A be an external dataset, and B be OpenStreetMap data. :
  --output-josm-file [OUTOSC]
                        Output OpenStreetMap change proposal in JOSM file
                        format

------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
    geojsondiff --output-diff-geojson=data/tmp/diff-points-ab.geojson --output-diff-tsv=data/tmp/diff-points-ab.tsv --output-diff-csv=data/tmp/diff-points-ab.csv --output-log=data/tmp/diff-points-ab.log.txt --tolerate-distance=1000 tests/data/data-points_a.geojson tests/data/data-points_b.geojson

GeoJSON (center point) example with overpass . . . . . . . . . . . . . . . . .
    [out:json][timeout:25];
    {geocodeArea:Santa Catarina}->.searchArea;
    (
    nwr["plant:source"="hydro"](area.searchArea);
    );
    convert item ::=::,::geom=geom(),_osm_type=type();
    out center;

------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------

```