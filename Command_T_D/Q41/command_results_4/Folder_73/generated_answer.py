def identical_elements(a, b):
    return set(x for x in range(min(len(a), len(b)), max(len(a), len(b)) + 1) if a[x] in b and a[x] not in a[:18] and a[x] not in a[93:])
