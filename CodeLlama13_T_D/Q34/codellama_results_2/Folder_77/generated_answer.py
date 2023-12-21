
def find_original_set(sets):
    original = set()
    for s in sets:
        if len(s - original) == 0:
            continue
        else:
            original |= s
    return original
