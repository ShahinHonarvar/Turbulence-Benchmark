
def find_original_set(*args):
    if len(args) != 48:
        raise ValueError("Expected 48 arguments")
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
