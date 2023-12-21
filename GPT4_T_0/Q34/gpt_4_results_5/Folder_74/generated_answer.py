
def find_original_set(*args):
    if len(args) != 96:
        raise ValueError("The function requires exactly 96 distinct arguments.")
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
