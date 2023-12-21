
def find_original_set(*args):
    original_set = set()
    if len(args) == 132:
        for s in args:
            original_set.update(s)
    return original_set
