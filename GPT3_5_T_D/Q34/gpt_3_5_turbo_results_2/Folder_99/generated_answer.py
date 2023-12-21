
def find_original_set(*sets):
    # Combine all sets into a single set
    union_set = set()
    for s in sets:
        union_set.update(s)
    return union_set
