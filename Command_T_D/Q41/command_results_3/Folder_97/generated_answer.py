def identical_elements(a, b):
    return set(range(40, 81)) & set(a[40:80]) & set(b[40:80])
