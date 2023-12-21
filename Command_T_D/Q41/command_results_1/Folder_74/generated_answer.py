def identical_elements(x, y):
    return set(i for i in range(17, 78 + 1) if x[i] in y and y[i] in x)
