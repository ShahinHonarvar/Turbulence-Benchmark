
def find_original_set(*args):
    if len(args) != 57:
        raise ValueError("The function needs exactly 57 sets of integers as argument")
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError("All arguments must be sets of integers")
        original_set = original_set.union(arg)
    return original_set
