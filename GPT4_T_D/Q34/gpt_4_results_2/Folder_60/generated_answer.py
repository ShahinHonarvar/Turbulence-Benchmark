
def find_original_set(*sets):
    original_set = set()
    for set_item in sets:
        original_set = original_set.union(set_item)
    return original_set
