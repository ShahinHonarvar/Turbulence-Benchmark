def identical_elements(a, b):
    return set(i for i in range(55, 98) for j in range(55, 98) if a[i] == b[j])
