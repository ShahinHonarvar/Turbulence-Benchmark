
def find_original_set(*args):
    original_set = set()
    if len(args) == 132:
        for arg in args:
            original_set.update(arg)
    return original_set
