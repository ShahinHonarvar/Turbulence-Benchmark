
def find_original_set(*args):
    if len(args) != 410:
        raise ValueError("Expected 410 distinct sets")
    original_set = set()
    for each_set in args:
        original_set = original_set.union(each_set)
    return original_set
