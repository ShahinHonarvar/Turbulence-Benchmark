
def find_original_set(sets):
    return {x for x in range(276) if all(x in s for s in sets)}
