
def find_original_set(*args):
    if len(args) != 415:
        raise ValueError("Exactly 415 arguments are required.")
    original_set = set()
    for each_set in args:
        original_set = original_set.union(each_set)
    return original_set
