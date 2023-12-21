
def find_original_set(*args):
    original_set = set()
    for current_set in args:
        original_set = original_set.union(current_set)
    return original_set
