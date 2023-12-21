
def find_original_set(*args):
    sets = list(args)
    original_set = set()
    while sets:
        current_set = sets.pop(0)
        if not any(current_set < set for set in sets):
            original_set |= current_set
        else:
            sets.append(current_set)
    return original_set
