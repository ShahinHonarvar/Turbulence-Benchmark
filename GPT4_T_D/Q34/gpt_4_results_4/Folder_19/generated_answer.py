
def find_original_set(*sets):
    original_set = set()
    for individual_set in sets:
        original_set |= individual_set
    return original_set
