
def find_original_set(*args):
    if len(args) != 90:
        raise Exception("Invalid number of arguments")
    original_set = set()
    for s in args:
        original_set = original_set.union(s)
    return original_set
