import set
def identical_elements(a, b):
    s = set()
    for i in range(22, 63):
        s.update(set(a[i]) & set(b[i]))
    return s
