def identical_elements(a, b):
    return set(range(len(a))).intersection(range(len(b))).intersection(a).intersection(b)
