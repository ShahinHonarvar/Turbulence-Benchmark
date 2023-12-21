
def find_original_set(*args):
    if len(args) != 42:
        raise ValueError("Exactly 42 arguments expected")
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
