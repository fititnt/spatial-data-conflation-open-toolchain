#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  overpassql2osmf.py
#
#         USAGE:  overpassql2osmf --help
#
#   DESCRIPTION:  ---
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - python3
#                   - pip install pandas (https://pandas.pydata.org/)
#          BUGS:  ---
#         NOTES:  ---
#       AUTHORS:  Emerson Rocha <rocha[at]ieee.org>
# COLLABORATORS:  ---
#
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v0.2.0
#       CREATED:  2023-04-26 01:04 BRT
#      REVISION:  ---
# ==============================================================================

# ./src/gisconflation/overpassql2osmf.py --help
# ./src/gisconflation/overpassql2osmf.py tests/data/cnes.overpassql tests/temp/cnes.osm.json

import os
import sys
import argparse

import requests

# import pandas as pd

__VERSION__ = "0.2.0"
PROGRAM = "overpassql2osmf"
DESCRIPTION = """
------------------------------------------------------------------------------
{0} v{1} convert Overpass Query Language to am OSM File (XML)

------------------------------------------------------------------------------
""".format(
    PROGRAM, __VERSION__
)

__EPILOGUM__ = """
------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
    {0} input.csv output.xlsx
------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
""".format(
    PROGRAM
)

STDIN = sys.stdin.buffer
OVERPASS_INTERPRETER = os.getenv(
    "OVERPASS_INTERPRETER", "https://overpass-api.de/api/interpreter"
)


class Cli:
    def __init__(self):
        """
        Constructs all the necessary attributes for the Cli object.
        """
        self.pyargs = None
        self.EXIT_OK = 0
        self.EXIT_ERROR = 1
        self.EXIT_SYNTAX = 2

    def make_args(self):
        """make_args"""
        parser = argparse.ArgumentParser(
            prog=PROGRAM,
            description=DESCRIPTION,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=__EPILOGUM__,
        )

        parser.add_argument(
            "input_query", help="Input OverpassQL query or path to .overpassql file"
        )
        # parser.add_argument("output_file", help="Output XLSX")

        # # @see https://stackoverflow.com/questions/41669690/how-to-overcome-the-limit-of-hyperlinks-in-excel
        # parser.add_argument(
        #     "--hiperlink",
        #     help="Add hiperlink to column names if they have non-empty value. "
        #     "alredy are mached with each other. "
        #     "Use '||' to deparate colum name from the URL. "
        #     "Add {value} as part of the URL for placeholder of external link. "
        #     "Accept multiple values. "
        #     "Example: "
        #     "--pivot-key-main='colum_name||http://example.com/page/{value}'",
        #     dest="hiperlink",
        #     nargs="?",
        #     action="append",
        # )

        return parser.parse_args()

    def execute_cli(self, pyargs, stdin=STDIN, stdout=sys.stdout, stderr=sys.stderr):
        query = pyargs.input_query
        if pyargs.input_query.endswith(".overpassql"):
            with open(pyargs.input_query, "r") as file:
                query = file.read()

        result_str = overpassql2osmf(
            query,
        )
        print(result_str)
        # with open(pyargs.output_file, "w") as file:
        #     file.write(result_str)

        return self.EXIT_OK


def overpassql2osmf(input_query: str):
    """overpassql2osmf
    @see https://xlsxwriter.readthedocs.io/example_pandas_autofilter.html

    Args:
        input_query (str): Input CSV file
        output_file (str): Output XLSX
    """

    print("TODO")
    print(input_query)

    payload = {"data": input_query}

    r = requests.post(OVERPASS_INTERPRETER, data=payload)
    # print(output_file)
    print(r)
    print(r.content)
    return "todo"


def parse_argument_values(arguments: list, delimiter: str = "||") -> dict:
    if not arguments or len(arguments) == 0 or not arguments[0]:
        return None

    result = {}
    for item in arguments:
        if item.find(delimiter) > -1:
            _key, _val = item.split(delimiter)
            result[_key] = _val
        else:
            result[_key] = True
    return result


def exec_from_console_scripts():
    main = Cli()
    args = main.make_args()
    main.execute_cli(args)


if __name__ == "__main__":
    cli_main = Cli()
    args = cli_main.make_args()
    cli_main.execute_cli(args)
