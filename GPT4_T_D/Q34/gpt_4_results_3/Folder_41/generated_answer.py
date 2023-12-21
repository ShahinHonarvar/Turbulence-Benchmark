
def find_original_set(*args):
    assert len(args) == 20, "Exactly 20 sets are required"
    original_set = set.union(*args)
    return original_set
