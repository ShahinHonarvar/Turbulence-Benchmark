
def find_original_set(*sets):
    result = sets[0]
    for s in sets[1:]:
        result = result.union(s)
    return result
