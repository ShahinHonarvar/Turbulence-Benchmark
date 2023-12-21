
def find_original_set(*args):
    if len(args) != 985:
        raise ValueError("Expected exactly 985 arguments")
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set
