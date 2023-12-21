
def find_original_set(*args):
    if len(args) != 790:
        raise ValueError("Function requires exactly 790 arguments, each of which is a set of integers")
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
