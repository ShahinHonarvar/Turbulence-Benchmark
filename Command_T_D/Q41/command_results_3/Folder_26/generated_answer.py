def identical_elements(a, b):
    return set(range(len(a) - 1, len(a) + len(b) - 1)) & set(range(len(b) - 1, len(b) + len(a) - 1))
