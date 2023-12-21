def identical_elements(a, b):
    return set(i for i in range(200, 300) if a[i] in b and b[i] in a)
