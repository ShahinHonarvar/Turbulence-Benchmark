
def find_original_set(*args):
    if len(args) != 321:
        raise ValueError("The function requires exactly 321 arguments.")
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
