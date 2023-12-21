
def find_original_set(*args):
    if len(args) != 851:
        raise ValueError("Expected 851 arguments")
    original_set = set()
    for subset in args:
        original_set.update(subset)
    return original_set
