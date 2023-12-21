
def find_original_set(*args):
    if len(args) != 73:
        raise ValueError("The function requires exactly 73 arguments.")
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
