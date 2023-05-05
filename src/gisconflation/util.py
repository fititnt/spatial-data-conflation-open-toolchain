import re
import string

# https://pypi.org/project/Levenshtein/
# pip install levenshtein
import Levenshtein


class AttributesEditor:
    """Edit attributes of a dictionary"""

    def __init__(
        self,
        rename_attr: dict = None,
        value_fixed: dict = None,
        value_name_place: list = None,
        normalize_prop: bool = True,
    ) -> None:
        self.rename_attr = rename_attr
        self.value_fixed = value_fixed
        self.value_name_place = value_name_place
        self.normalize_prop = normalize_prop

    def edit(self, item: dict) -> dict:
        result = item

        # print('teste')
        # raise NotImplementedError
        # if self.rename_attr is not None and len(self.rename_attr.keys()) > 0:
        if self.rename_attr is not None:
            for key, val in self.rename_attr.items():
                if key in result:
                    result[val] = result.pop(key)

        # if isinstance(self.value_fixed, list) and len(self.value_fixed) > 0:
        if self.value_fixed:
            for key, val in self.value_fixed.items():
                result[key] = val

        # if isinstance(self.value_name_place, list) and len(self.value_name_place) > 0:
        if self.value_name_place:
            for key in self.value_name_place:
                if key not in result:
                    continue
                _value = _zzz_format_name_place_br(result[key])
                if _value:
                    result[key] = _value
                else:
                    result[key] = ""

        if self.normalize_prop:
            prop_new = {}
            # print(result["properties"])
            for key, val in sorted(result.items()):
                if isinstance(val, str):
                    val = val.strip()
                if not val:
                    continue
                prop_new[key] = val
            result = prop_new

        return result


class LevenshteinHelper:
    """LevenshteinHelper is ...
    @see https://maxbachmann.github.io/Levenshtein/levenshtein.html
    """

    def __init__(self) -> None:
        pass

    def test(self) -> str:
        """_summary_

        Returns:
            str: _description_

        >>> lh = LevenshteinHelper()
        >>> lh.test()
        'test'
        """
        # return Levenshtein.distance("teste", "testeee")
        return "test"


# def parse_argument_values(arguments: list, delimiter: str = "||") -> dict:
def parse_argument_values(
    arguments: list, delimiter: str = "|||", delimiter2: str = "||"
) -> dict:
    if not arguments or len(arguments) == 0 or not arguments[0]:
        return None

    result = {}
    for item in arguments:
        # print('__', item, item.find(delimiter))
        if item.find(delimiter) > -1:
            _key, _val = item.split(delimiter)
            if _val.find(delimiter2) > -1:
                _val = item.split(_val)
            result[_key] = _val
        else:
            result[item] = True

    # print('__f', result)
    return result


# @TODO refactor this code and allow localization of values
def _zzz_format_name_place_br(value: str):
    if not value or not isinstance(value, str):
        return value

    term = string.capwords(value.strip())
    term2 = re.sub("\\s\\s+", " ", term)

    # @TODO deal with Do Da De

    term2 = term2.replace(" Da ", " da ")
    term2 = term2.replace(" De ", " de ")
    term2 = term2.replace(" Do ", " do ")

    return term2


def _zzz_format_phone_br(value: str):
    if not value:
        return False

    if value.startswith("+"):
        return value

    # @TODO deal with more than one number

    if value.startswith("(") and value.find(")") > -1:
        _num_com_ddd = "".join(filter(str.isdigit, value))

        _regiao = _num_com_ddd[0:2]
        _num_loc = _num_com_ddd[2:]
        _num_loc_p2 = _num_loc[-4:]
        _num_loc_p1 = _num_loc.replace(_num_loc_p2, "")
        # return "+55 " + _regiao + ' ' + _num_com_ddd[2:]
        return "+55 " + _regiao + " " + _num_loc_p1 + " " + _num_loc_p2

    # if value.isnumeric():
    #     if len(value) == 8:
    #         return re.sub(r"(\d{5})(\d{3})", r"\1-\2", value)
    return False
