
def find_original_set(*args):
    if len(args) != 74:
        raise ValueError("Function should take exactly 74 arguments")
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError("All arguments must be sets of integers")
        original_set = original_set.union(arg)
    return original_set
