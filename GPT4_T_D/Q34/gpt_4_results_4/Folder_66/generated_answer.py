
def find_original_set(*args):
    assert len(args) == 25, "Only 25 sets are allowed"
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set
