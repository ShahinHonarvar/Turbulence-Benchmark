
def find_original_set(*args):
    return set(range(1, max(max(a) for a in args)+1))
