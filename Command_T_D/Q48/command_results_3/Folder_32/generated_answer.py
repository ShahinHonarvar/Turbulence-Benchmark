
def return_binary_or_hexa(tup):
    idx_a, idx_b = 86, 90
    idx_s = tup.index(idx_a)
    idx_e = tup.index(idx_b)
    res = sum(tup[idx_s + 1 : idx_e - 1])
    if res % 2:
        return str(res).zfill(len(str(res)))
    return hex(res).zfill(len(hex(res)))
