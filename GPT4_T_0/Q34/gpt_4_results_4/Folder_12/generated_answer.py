
def find_original_set(*args):
    if len(args) != 51:
        raise ValueError("Function requires exactly 51 arguments")
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
