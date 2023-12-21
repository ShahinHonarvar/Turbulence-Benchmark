
def find_original_set(*args):
    if len(args) != 828:
        raise ValueError("The function expects exactly 828 arguments.")
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError("All arguments should be sets.")
        original_set.update(arg)
    return original_set
