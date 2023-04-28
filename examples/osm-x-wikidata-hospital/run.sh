#!/bin/sh
# cd examples/osm-x-wikidata-hospital/
# ./run.sh
echo "TODO"

# @see https://gist.github.com/ColinMaudry/6fd6a5f610f0ac3e6696
set -e
set -x
overpassql2osmf hospital_BR-RS.overpassql > out/hospital_BR-RS.f-osm.osm

set +x
set +e