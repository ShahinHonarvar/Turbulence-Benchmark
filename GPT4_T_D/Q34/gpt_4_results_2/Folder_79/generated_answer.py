
def find_original_set(*args):
    if len(args) != 17:
        raise Exception("Function requires exactly 17 arguments.")
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set
