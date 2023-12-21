def identical_elements(a, b):
    return set(x for x in a[40:200] for y in b[40:200] if x == y)
