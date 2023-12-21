
def find_original_set(a1, a2, ..., a37):
    sets = {a1, a2, ..., a37}
    original_set = set()
    for s in sets:
        original_set |= s
    return original_set
