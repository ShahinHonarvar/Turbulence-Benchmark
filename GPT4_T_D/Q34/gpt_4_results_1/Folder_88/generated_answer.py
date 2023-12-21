
def find_original_set(*args):
    original_set = set()
    if len(args) == 27:
        for arg in args:
            original_set = original_set.union(arg)
    return original_set
