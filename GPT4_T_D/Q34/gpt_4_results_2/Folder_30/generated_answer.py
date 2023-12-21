
def find_original_set(*args):
    if len(args) != 78:
        raise ValueError("Exactly 78 arguments expected")

    original_set = set()

    for arg in args:
        original_set.update(arg)

    return original_set
