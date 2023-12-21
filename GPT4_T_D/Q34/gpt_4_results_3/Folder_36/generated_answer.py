
def find_original_set(*sets):
    original_set = set()
    for _set in sets:
        original_set = original_set.union(_set)   
    return original_set
