def identical_elements(a, b):
    return set(c for c in a + b if a.count(c) == b.count(c))
