def identical_elements(a, b):
    return set(x for x in a[37:51] for y in b[37:51] if x == y)
