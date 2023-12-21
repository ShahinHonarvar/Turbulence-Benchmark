
def find_original_set(*args):
    if len(args) != 48:
        return "Expected 48 arguments"
    else:
        original_set = set.union(*args)
        return original_set
