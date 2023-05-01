#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  geojsonmerger.py
#
#         USAGE:  geojsonmerger --help
#                 ./src/gisconflation/geojsonmerger.py --help
#
#   DESCRIPTION:  ---
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - python3
#          BUGS:  ---
#         NOTES:  ---
#       AUTHORS:  Emerson Rocha <rocha[at]ieee.org>
# COLLABORATORS:  ---
#
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v0.1.0
#       CREATED:  2023-04-28 14:17 BRT
# ==============================================================================

import argparse

# import csv
# import dataclasses
import json
import sys

# import logging
from typing import List, Type

from .util import AttributesEditor, parse_argument_values

# from haversine import haversine, Unit

# # from shapely.geometry import Polygon, Point
# from shapely.geometry import Polygon
# from xml.sax.saxutils import escape


__VERSION__ = "0.1.0"

PROGRAM = "geojsonmerger"
DESCRIPTION = """
------------------------------------------------------------------------------
[DRAFT] GeoJSON simple merger

Merge extra attributes from an GeoJSON (likely the one with more metadata, but
not accurate geometry) into another GeoJSON.

------------------------------------------------------------------------------
""".format(
    __file__
)

# https://www.rfc-editor.org/rfc/rfc7946
# The GeoJSON Format
# https://www.rfc-editor.org/rfc/rfc8142
# GeoJSON Text Sequences

# __EPILOGUM__ = ""
__EPILOGUM__ = """
------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
    {0} --help

------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
""".format(
    PROGRAM
)

STDIN = sys.stdin.buffer

# MATCH_EXACT = 1
# MATCH_NEAR = 3


class Cli:
    """Main CLI parser"""

    def __init__(self):
        """
        Constructs all the necessary attributes for the Cli object.
        """
        self.pyargs = None
        self.EXIT_OK = 0
        self.EXIT_ERROR = 1
        self.EXIT_SYNTAX = 2

    def make_args(self):
        """make_args

        Args:
            hxl_output (bool, optional): _description_. Defaults to True.
        """
        parser = argparse.ArgumentParser(
            prog=PROGRAM,
            description=DESCRIPTION,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=__EPILOGUM__,
        )

        parser.add_argument("geodataset_a", help="GeoJSON dataset 'A'")
        parser.add_argument("geodataset_b", help="GeoJSON dataset 'B'")

        # # @TODO maybe implement GeoJSONSeq
        # parser.add_argument("input", help="Input GeoJSON / GeoJSONSeq. Use - for stdin")
        # # parser.add_argument("geodataset_b", help="GeoJSON dataset 'B'")

        parser.add_argument(
            "--format-output",
            help="Path to output file",
            dest="format_output",
            default="auto",
            required=False,
            choices=["auto", "geojson", "geojsonseq"],
            nargs="?",
        )

        edit = parser.add_argument_group("Change properties from each item")

        edit.add_argument(
            "--rename-attribute",
            help="Rename attribute (if exist). "
            "Use '||' to divide the source key and target key. "
            "Accept multiple values. "
            "Example: "
            "--rename-attribute='NAME|||name' --rename-attribute='CITY|||addr:city'",
            dest="rename_attr",
            nargs="?",
            action="append",
        )

        # Old versions of csv2geojson uses only one |
        edit.add_argument(
            "--value-fixed",
            help="Define a fixed string for every value of a column, "
            "For multiple, use multiple times this parameter. "
            "Source vs destiny column must be divided by |||. "
            "Example: <[ --value-fixed='source|||BR:DATASUS' ]>",
            dest="value_fixed",
            nargs="?",
            # type=lambda x: x.split("||"),
            action="append",
            default=None,
        )

        edit.add_argument(
            "--value-norm-name-place",
            help="Column to normalize value (strategy: name of place). "
            "Accept multiple options. Example: "
            "--value-norm-name-place='name' --value-norm-name-place='alt_name'",
            dest="value_name_place",
            nargs="?",
            # type=lambda x: x.split("||"),
            action="append",
            default=None,
        )

        filter = parser.add_argument_group("Options for filter input items completely")

        return parser.parse_args()

    def execute_cli(self, pyargs, stdin=STDIN, stdout=sys.stdout, stderr=sys.stderr):
        # logger = logging.getLogger()
        # logger.setLevel(logging.INFO)
        # if pyargs.outlog:
        #     fh = logging.FileHandler(pyargs.outlog)
        #     logger.addHandler(fh)
        # else:
        #     ch = logging.StreamHandler()
        #     logger.addHandler(ch)

        # normalize_prop = True
        # skip_invalid_geometry = True

        # # raise ValueError(parse_argument_values(pyargs.value_fixed))
        # # print(parse_argument_values(pyargs.value_fixed))

        # gitem = GeoJSONItemEditor(
        #     rename_attr=parse_argument_values(pyargs.rename_attr),
        #     value_fixed=parse_argument_values(pyargs.value_fixed),
        #     value_name_place=pyargs.value_name_place,
        #     normalize_prop=normalize_prop,
        #     skip_invalid_geometry=skip_invalid_geometry,
        # )
        # gedit = GeoJSONFileEditor(pyargs.input, gitem)
        # gedit.output()

        # skip_invalid_geometry: True

        # # geodiff.debug()
        gmerger = GeoJSONMerger(
            geodataset_a=pyargs.geodataset_a,
            geodataset_b=pyargs.geodataset_b,
            # skip_invalid_geometry=True,
        )
        # print("TODO")

        gmerger.output()
        # gmerger.debug()
        return self.EXIT_OK


class GeoJSONMerger:
    def __init__(self, geodataset_a, geodataset_b) -> None:
        self.geodataset_a = geodataset_a
        self.geodataset_b = geodataset_b

        # @TODO make it flexible
        self.key_a = "ref:CNES"
        self.key_b = "CO_CNES"

        self.in_a = []
        self.in_b = []
        self.out = []
        self.out_dict = {}

        self._init_a()
        self._init_b()

    def _init_a(self) -> None:
        a_str = self._loader_temp(self.geodataset_a)

        a_data = json.loads(a_str)
        for item in a_data["features"]:
            if not "properties" in item or not item["properties"]:
                raise SyntaxError(item)

            if not self.key_a in item["properties"]:
                raise SyntaxError([self.key_a, item])

            key_active = str(item["properties"][self.key_a])
            if key_active in self.out_dict:
                # Improve this err handling
                print(f"Repeated value {key_active}")
            self.out_dict[key_active] = item
            # print(item)

    def _init_b(self) -> None:
        b_str = self._loader_temp(self.geodataset_b)

        b_data = json.loads(b_str)

        for item in b_data["features"]:
            if not "properties" in item or not item["properties"] or not isinstance(item["properties"], dict):
                continue
                # raise SyntaxError(item)

            if not self.key_b in item["properties"]:
                raise SyntaxError([self.key_b, item])

            key_active = str(item["properties"][self.key_b])

            if key_active not in self.out_dict:
                continue

            # raise ValueError('deu')
            # print(key_active, type(key_active))
            # print(self.out_dict[key_active])
            # print('')
            # print(self.out_dict[key_active]["properties"])
            # print(item)

            _props = self.out_dict[key_active]["properties"]

            for _key, _val in item["properties"].items():
                # @TODO allow some filtering
                _props[_key] = _val

            # _props = {
            #     **self.out_dict[key_active]["properties"],
            #     **item["properties"][self.key_b],
            # }
            # self.out_dict[key_active]["properties"].update(
            #     item["properties"][self.key_b]
            # )

    def _loader_temp(self, input_ptr: str):
        # @TODO make this efficient for very large files
        data = None
        if input_ptr == "-":
            temp = []
            for line in sys.stdin:
                # temp.append(line.strip())
                temp.append(line.rstrip())
                # temp.append(line)

            data = "\n".join(temp)
        else:
            with open(input_ptr, "r") as _file:
                data = _file.read()
            # pass

        return data

    def debug(self):
        print("todo")

    def output(self):
        # @TODO keep other metadata at top level, if exist
        print('{"type": "FeatureCollection", "features": [')
        count = len(self.out_dict.keys())
        for _key, item in self.out_dict.items():
            count -= 1
            line_str = json.dumps(item, ensure_ascii=False)
            if count > 0:
                line_str += ","
            print(line_str)
        print("]}")


# geojsonmerger tests/temp/dataset_a.geojson tests/temp/dataset_b.geojson
# ./src/gisconflation/geojsonmerger.py tests/data/geojson-simple.geojson
# cat tests/data/geojson-simple.geojson | ./src/gisconflation/geojsonmerger.py -
# ./src/gisconflation/geojsonmerger.py tests/data/geojson-seq.geojsonl
class GeoJSONFileEditor:
    """geojsonmergeror

    @TODO implement read line-by-line large files (in special GeoJSONSeq)
    """

    def __init__(self, input_ptr: str, gitem: Type["GeoJSONItemEditor"]) -> None:
        self.gitem = gitem
        self.inputdata = self._loader_temp(input_ptr)
        # pass

    def _loader_temp(self, input_ptr: str):
        # @TODO make this efficient for very large files
        data = None
        if input_ptr == "-":
            temp = []
            for line in sys.stdin:
                # temp.append(line.strip())
                temp.append(line.rstrip())
                # temp.append(line)

            data = "\n".join(temp)
        else:
            with open(input_ptr, "r") as _file:
                data = _file.read()
            # pass

        return data

    def output(self):
        json_data = json.loads(self.inputdata)
        if not json_data or "features" not in json_data:
            raise SyntaxError("bad input data")

        result = {"features": []}
        for item in json_data["features"]:
            edited_item = self.gitem.edit(item)
            if edited_item is not False:
                result["features"].append(edited_item)

        # print(self.inputdata)
        # print(json_data)

        # @TODO keep other metadata at top level, if exist
        print('{"type": "FeatureCollection", "features": [')
        count = len(json_data["features"])
        for item in json_data["features"]:
            count -= 1
            line_str = json.dumps(item, ensure_ascii=False)
            if count > 0:
                line_str += ","
            print(line_str)
        print("]}")

        # print(json.dumps(result, ensure_ascii=False))


class GeoJSONItemEditor:
    def __init__(
        self,
        rename_attr: dict = None,
        value_fixed: dict = None,
        value_name_place: list = None,
        normalize_prop: bool = True,
        skip_invalid_geometry: bool = True,
    ) -> None:
        self.rename_attr = rename_attr
        self.normalize_prop = normalize_prop
        self.value_fixed = value_fixed
        self.value_name_place = value_name_place
        self.skip_invalid_geometry = skip_invalid_geometry

        self._attr_editor = AttributesEditor(
            rename_attr=rename_attr,
            value_fixed=value_fixed,
            value_name_place=value_name_place,
            normalize_prop=normalize_prop,
        )

        # print(self.rename_attr)
        # pass

    def edit(self, item: dict):
        # return item
        # print(item)
        result = item

        if self.skip_invalid_geometry:
            if (
                not item
                or not isinstance(item, dict)
                or "geometry" not in item
                or not item["geometry"]
                or "coordinates" not in item["geometry"]
                # or not item["geometry"]["coordinates"]
            ):
                # @TODO make better checks, like if is Type=Point, etc
                return False

        if "properties" in result:
            result["properties"] = self._attr_editor.edit(result["properties"])

            # if self.rename_attr is not None and len(self.rename_attr.keys()) > 0:
            #     for key, val in self.rename_attr.items():
            #         if key in result["properties"]:
            #             result["properties"][val] = result["properties"].pop(key)

            # if self.normalize_prop:
            #     prop_new = {}
            #     # print(result["properties"])
            #     for key, val in sorted(result["properties"].items()):
            #         if isinstance(val, str):
            #             val = val.strip()
            #         if not val:
            #             continue
            #         prop_new[key] = val
            #     result["properties"] = prop_new
        return result


# def parse_argument_values(arguments: list, delimiter: str = "||") -> dict:
#     if not arguments or len(arguments) == 0 or not arguments[0]:
#         return None

#     result = {}
#     for item in arguments:
#         # print('__', item, item.find(delimiter))
#         if item.find(delimiter) > -1:
#             _key, _val = item.split(delimiter)
#             result[_key] = _val
#         else:
#             result[item] = True

#     # print('__f', result)
#     return result


def exec_from_console_scripts():
    main = Cli()
    args = main.make_args()
    main.execute_cli(args)


if __name__ == "__main__":
    main = Cli()
    args = main.make_args()
    main.execute_cli(args)
