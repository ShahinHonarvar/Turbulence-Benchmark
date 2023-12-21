def identical_elements(a, b):
    return set(x for x in a[22:50] for y in b[22:50] if x == y)
