
def find_original_set(*args):
    if len(args) != 40:
        raise ValueError("Function requires exactly 40 arguments")
    result = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError("All arguments should be sets")
        for element in arg:
            if not isinstance(element, int):
                raise ValueError("All elements in the sets should be integers")
            result.add(element)
    return result
