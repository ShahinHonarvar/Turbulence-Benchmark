def identical_elements(x, y):
    if len(x) != len(y):
        return set()
    z = set(x[30:48])
    return z & set(y[30:48])
