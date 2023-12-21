
def find_original_set(*sets):
    if len(sets) != 849:
        return "The function should have exactly 849 sets"

    original_set = set()

    for curr_set in sets:
        original_set = original_set.union(curr_set)

    return original_set
