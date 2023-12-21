
def find_original_set(A, B, C, D):
    return {a for a in A | B | C | D}
