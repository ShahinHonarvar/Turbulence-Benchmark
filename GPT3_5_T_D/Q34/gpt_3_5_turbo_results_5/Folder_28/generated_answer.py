
def find_original_set(*args):
    sets = list(args)
    for i in sets:
        if isinstance(i, set) == False:
            return None
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set
