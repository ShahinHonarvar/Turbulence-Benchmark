
def find_original_set(*args):
    original_set = set()
    for s in args:
        original_set = original_set.union(s)
    return original_set
