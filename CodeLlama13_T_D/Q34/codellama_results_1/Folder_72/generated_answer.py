
def find_original_set(args):
    original = set()
    for arg in args:
        original |= arg
    return original
