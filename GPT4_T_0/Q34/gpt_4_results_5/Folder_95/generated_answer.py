
def find_original_set(*args):
    if len(args) != 88:
        raise ValueError("The function requires exactly 88 arguments.")
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
