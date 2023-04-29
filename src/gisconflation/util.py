class AttributesEditor:
    """Edit attributes of a dictionary"""

    def __init__(
        self,
        rename_attr: dict = None,
        normalize_prop: bool = True,
    ) -> None:
        self.rename_attr = rename_attr
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
