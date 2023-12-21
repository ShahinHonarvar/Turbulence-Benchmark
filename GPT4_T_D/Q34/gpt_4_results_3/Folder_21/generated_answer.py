
def find_original_set(*args):
    if len(args) != 851:
        raise ValueError("Needs exactly 851 arguments.")
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError("All arguments should be sets.")
        original_set = original_set.union(arg)
    return original_set
