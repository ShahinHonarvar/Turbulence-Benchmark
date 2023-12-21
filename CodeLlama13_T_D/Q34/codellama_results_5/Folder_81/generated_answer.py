
def find_original_set(sets):
    return min([{i for s in sets for i in s}], key=len)
