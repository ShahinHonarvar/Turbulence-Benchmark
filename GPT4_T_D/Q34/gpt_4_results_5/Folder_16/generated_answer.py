
def find_original_set(*sets):
    if len(sets) != 321:
        raise ValueError("Function requires exactly 321 sets.")
    original_set = set.union(*sets)
    return original_set
