
def find_original_set(*args):
    if len(args) != 132:
        raise ValueError("Function requires exactly 132 arguments")

    original_set = set()
    for arg in args:
        original_set |= arg

    return original_set
