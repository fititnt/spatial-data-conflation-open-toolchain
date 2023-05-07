#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  dictionarymerger.py
#
#         USAGE:  ./scripts/dictionarymerger.py
#                 ./scripts/dictionarymerger.py --help
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
#       LICENSE:  GNU Affero General Public License v3.0 or later
#                 SPDX-License-Identifier: AGPL-3.0-or-later
#       VERSION:  v1.0.0
#       CREATED:  2023-05-06 22:24 BRT started, based on dictionarybuilder.py
#      REVISION:  --
# ==============================================================================

import argparse
import csv
import re
import sys


__VERSION__ = "1.0.0"
PROGRAM = "dictionarymerger"
DESCRIPTION = """
------------------------------------------------------------------------------
For 2 or more output dictionaries from dictionarybuilder, merge them.

Simple strategy is *append* (e.g. similar to unix cat command, but sort again
the values and check inconsistencies).

The additional strategy is *transpose* value from dictionary A directly on
result of dictoryary B. Example:

    Input 1: X -> Y
    Input 2: Y -> Z
    Output:  X -> Z

------------------------------------------------------------------------------
""".format(
    PROGRAM, __VERSION__
)

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

# Record separator
DICTIONARY_SEPARATOR = "␞"

STDIN = sys.stdin.buffer


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
        """make_args"""
        parser = argparse.ArgumentParser(
            prog=PROGRAM,
            description=DESCRIPTION,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=__EPILOGUM__,
        )


        # @see https://stackoverflow.com/questions/5373474/multiple-positional-arguments-with-python-and-argparse
        # @TODO deal with both simple contatenation and transposition
        #       do not need to implement on this tool advanced input normalization
        parser.add_argument("input", help="path to CSV file on disk. Use - for stdin")

        # parser.add_argument(
        #     "--input-delimiter",
        #     help="The input delimiter",
        #     dest="in_delimiter",
        #     default=",",
        #     required=False,
        #     nargs="?",
        # )

        # parser.add_argument(
        #     "--input-encoding",
        #     help="The input encoding",
        #     dest="in_encoding",
        #     default="utf-8",
        #     required=False,
        #     nargs="?",
        # )

        # parser.add_argument(
        #     "--input-fieldnames",
        #     help="If the input CSV does not have a header, specify here. "
        #     "Use | as separator (if a field de de facto have |, then use \|). "
        #     "Example: --input-fieldnames='field with \| on it|another field'",
        #     dest="in_fieldnames",
        #     # default="utf-8",
        #     required=False,
        #     nargs="?",
        # )

        # parser.add_argument(
        #     "--dict-target-key",
        #     help="Field name to represent the primary key to convert data "
        #     "Defaults to first column. Example: "
        #     "--dict-target-key='id'",
        #     dest="dict_target",
        #     required=False,
        #     nargs="?",
        # )

        # parser.add_argument(
        #     "--dict-source-key",
        #     help="Field name to be used as source to convert data to target key. "
        #     "If undefined, defaults to all fields which are not the "
        #     "--dict-target-key. Example: "
        #     "--dict-source-key='name' --dict-source-key='title' ",
        #     dest="dict_sources",
        #     action="append",
        #     required=False,
        #     nargs="?",
        # )

        # parser.add_argument(
        #     "--transform-uppercase",
        #     help="Force all source values to UPPERCASE",
        #     dest="t_uppercase",
        #     action="store_true",
        # )

        # parser.add_argument(
        #     "--transform-lowercase",
        #     help="Force all source values to lowercase",
        #     dest="t_lowercase",
        #     action="store_true",
        # )

        # parser.add_argument(
        #     "--transform-no-latin-accents",
        #     help="Remove some diacrilics of latin script",
        #     dest="t_nolatinaccents",
        #     action="store_true",
        # )

        parser.add_argument(
            "--ignore-warnings",
            help="Ignore some errors (duplicated key / ambiguous results)",
            dest="ignore_warnings",
            action="store_true",
        )

        return parser.parse_args()

    def execute_cli(self, pyargs, stdin=STDIN, stdout=sys.stdout, stderr=sys.stderr):
        # @TODO implement strict run (fail if repeated source falues)
        # @TODO implement UPPER, lower and remove-accents options

        # @TODO stdin does not yet allow non UTF8 customization (will pass as it is)
        # @see https://stackoverflow.com/questions/5004687
        with open(pyargs.input, "r", encoding=pyargs.in_encoding) if len(
            pyargs.input
        ) > 1 else sys.stdin as csvfile:
            if pyargs.in_fieldnames:
                _in_fieldnames = re.split(r"(?<!\\)\|", pyargs.in_fieldnames)
                # _in_fieldnames = re.split(r"", pyargs.in_fieldnames)

                reader = csv.DictReader(
                    csvfile, fieldnames=_in_fieldnames, delimiter=pyargs.in_delimiter
                )
            else:
                reader = csv.DictReader(csvfile, delimiter=pyargs.in_delimiter)

            # reader = csv.DictReader(csvfile, delimiter=pyargs.in_delimiter)

            firstline = next(reader)
            # print(firstline)

            _fieldnames = firstline.keys()
            # print(_fieldnames)

            if pyargs.dict_target:
                dict_target = pyargs.dict_target
            else:
                # dict_target = _fieldnames[0]
                dict_target = list(_fieldnames).pop(0)

            if pyargs.dict_sources:
                dict_sources = pyargs.dict_sources
            else:
                _temp = list(_fieldnames)
                _temp.remove(dict_target)
                dict_sources = _temp

            writer = csv.writer(
                sys.stdout, delimiter=DICTIONARY_SEPARATOR, quoting=csv.QUOTE_MINIMAL
            )

            outdict = {}
            # @TODO This part is a bit duplicated. Could be better.
            # #     Remove duplicated code
            for item in dict_sources:
                if not firstline[item] or len(firstline[item]) == 0:
                    continue

                _v = firstline[item].strip()
                _k = firstline[dict_target].strip()

                if pyargs.t_nolatinaccents:
                    _k = _k.lower()
                    # Obviously incomplete
                    _k = re.sub(r"[àáâãäå]", "a", _k)
                    _k = re.sub(r"[èéêë]", "e", _k)
                    _k = re.sub(r"[ìíîï]", "i", _k)
                    _k = re.sub(r"[òóôõö]", "o", _k)
                    _k = re.sub(r"[ñ]", "n", _k)
                    _k = re.sub(r"[ç]", "c", _k)

                if pyargs.t_lowercase:
                    _k = _k.lower()
                elif pyargs.t_uppercase:
                    _k = _k.upper()

                if _k in outdict and outdict[_k] != _v and not pyargs.ignore_warnings:
                    print(f"{_k} repeated", sys.stderr)

                outdict[_k] = _v

            for row in reader:
                for item in dict_sources:
                    if not row[item] or len(row[item]) == 0:
                        continue

                    _v = row[item].strip()
                    _k = row[dict_target].strip()

                    if pyargs.t_nolatinaccents:
                        _k = _k.lower()
                        # Obviously incomplete
                        _k = re.sub(r"[àáâãäå]", "a", _k)
                        _k = re.sub(r"[èéêë]", "e", _k)
                        _k = re.sub(r"[ìíîï]", "i", _k)
                        _k = re.sub(r"[òóôõö]", "o", _k)
                        _k = re.sub(r"[ñ]", "n", _k)
                        _k = re.sub(r"[ç]", "c", _k)

                    if pyargs.t_lowercase:
                        _k = _k.lower()
                    elif pyargs.t_uppercase:
                        _k = _k.upper()

                    if (
                        _k in outdict
                        and outdict[_k] != _v
                        and not pyargs.ignore_warnings
                    ):
                        print(f"{_k} repeated", sys.stderr)

                    outdict[_k] = _v

                    # outdict[firstline[item].strip()] = firstline[dict_target].strip()
                # writer.writerow(row)

            outdict_sorted = dict(sorted(outdict.items()))

            # print(outdict)
            # outdict

            for key, value in outdict_sorted.items():
                writer.writerow([key, value])

            # # writer.writeheader()
            # writer.writerow(firstline)

            # for row in reader:
            #     writer.writerow(row)

        return self.EXIT_OK


def exec_from_console_scripts():
    main = Cli()
    args = main.make_args()
    main.execute_cli(args)


if __name__ == "__main__":
    cli_2600 = Cli()
    args = cli_2600.make_args()
    # pyargs.print_help()

    # args.execute_cli(args)
    cli_2600.execute_cli(args)