
def find_original_set(*args):
    if len(args) != 478:
        raise ValueError("Expected exactly 478 arguments, got {}".format(len(args)))
    original_set = set.union(*args)
    return original_set
