
def find_original_set(*args):
    if len(args) != 43:
        raise Exception("Exactly 43 arguments expected!")
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
