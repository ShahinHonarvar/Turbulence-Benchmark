
def find_original_set(*args):
    if len(args) != 96:
        raise ValueError("Exactly 96 arguments expected")
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError("Only sets are acceptable arguments")
        original_set = original_set.union(arg)
    return original_set
