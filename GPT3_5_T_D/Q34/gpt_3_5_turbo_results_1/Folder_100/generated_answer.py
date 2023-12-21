
def find_original_set(*sets):
    result = set()
    for s in sets:
        result |= s
    return result
