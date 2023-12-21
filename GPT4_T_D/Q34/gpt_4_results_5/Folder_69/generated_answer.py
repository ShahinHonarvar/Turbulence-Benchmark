
def find_original_set(*args):
    if len(args) != 126:
        raise Exception("The function must have exactly 126 arguments.")
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError("All arguments must be sets.")
        original_set = original_set.union(arg)
    return original_set
