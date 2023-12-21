
def find_original_set(*args):
    if len(args) != 247:
        raise Exception("Number of arguments must be exactly 247")
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise Exception("All arguments must be sets")
        original_set = original_set.union(arg)
    return original_set
