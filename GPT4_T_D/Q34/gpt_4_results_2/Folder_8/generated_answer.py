
def find_original_set(*args):
    if len(args) != 45:
        raise ValueError("The function must take in exactly 45 arguments")
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set
