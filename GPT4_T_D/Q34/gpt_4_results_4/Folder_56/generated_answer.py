
def find_original_set(*args):
    if len(args) != 63:
        raise ValueError('Exactly 63 distinct arguments required')

    original_set = set()
    for s in args:
        original_set.update(s)

    return original_set
