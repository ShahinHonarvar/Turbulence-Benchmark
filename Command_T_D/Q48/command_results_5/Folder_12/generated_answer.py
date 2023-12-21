
def return_binary_or_hexa(tup):
    a, b = 16, 87
    idx = tup.index(a)
    idx_b = tup.index(b)
    mask = 0
    for i in range(idx + 1, idx_b):
        if i in tup:
            continue
        mask += 1
    if mask % 2:
        return format(mask, 'b')
    else:
        return format(mask, 'x')
