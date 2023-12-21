
def find_original_set(*args):
    if len(args) != 88:
        raise Exception("The function requires exactly 88 distinct sets")
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set
