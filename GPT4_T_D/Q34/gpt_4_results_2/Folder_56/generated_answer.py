
def find_original_set(*args):
    original_set = set()
    for sets in args:
        original_set.update(sets)
    return original_set
