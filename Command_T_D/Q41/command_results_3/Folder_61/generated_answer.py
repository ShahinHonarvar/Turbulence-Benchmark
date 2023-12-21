def identical_elements(x, y):
    return set(x + y).intersection(x[0:7] + y[0:7])
