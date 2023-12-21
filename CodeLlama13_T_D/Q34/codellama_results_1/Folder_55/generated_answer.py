
def find_original_set(a1, a2, ..., a33):
    sets = [a1, a2, ..., a33]
    original_set = set()
    for s in sets:
        if not s <= original_set:
            original_set |= s
    return original_set
