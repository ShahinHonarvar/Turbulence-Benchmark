
def find_original_set(a, b, c, d):
    return {x for s in (a, b, c, d) for x in s}
