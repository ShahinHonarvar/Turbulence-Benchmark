def identical_elements(a, b):
    return set(range(40, 200 + 1)) & set(a[40:200+1]) & set(b[40:200+1])
