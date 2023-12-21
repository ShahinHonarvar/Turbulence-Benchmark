
def find_original_set(*args):
    if len(args) != 64:
        raise ValueError("Exactly 64 distinct sets are required")

    original_set = set()
    for subset in args:
        original_set.update(subset)

    return original_set
