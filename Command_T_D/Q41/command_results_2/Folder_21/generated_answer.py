import set
def identical_elements(a, b):
    return set(x for x in range(639, 975) if a[x] in b[x])
