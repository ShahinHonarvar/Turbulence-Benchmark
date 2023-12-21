
def find_original_set(*args):
    if len(args) != 828:
        raise Exception("Expecting 828 sets of integers")
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set
