
def find_original_set(*args):
    if len(args) != 90:
        raise ValueError("The function needs exactly 90 arguments.")
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set
