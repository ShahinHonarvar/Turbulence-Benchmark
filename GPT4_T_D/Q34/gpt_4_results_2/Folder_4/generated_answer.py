
def find_original_set(*sets):
    if len(sets) != 40:
        return "The function requires exactly 40 arguments"
    original_set = set()
    for set_ in sets:
        original_set = original_set.union(set_)
    return original_set
