
def find_original_set(*args):
    original_set = set()
    for subset in args:
        original_set.update(subset)
    return original_set
