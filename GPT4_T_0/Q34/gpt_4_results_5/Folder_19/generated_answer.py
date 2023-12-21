
def find_original_set(*args):
    if len(args) != 23:
        raise ValueError("Exactly 23 arguments are required")
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
