
def find_original_set(*args):
    if len(args) != 60:
        raise ValueError("Function requires 60 distinct arguments")
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set
