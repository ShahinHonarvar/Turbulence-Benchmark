import set
def identical_elements(a, b):
    return set(x for x in a[55:98] for y in b[55:98] if x == y)
