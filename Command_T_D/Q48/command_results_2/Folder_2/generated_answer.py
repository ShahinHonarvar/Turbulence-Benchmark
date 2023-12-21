
def return_binary_or_hexa(tup):
    a, b = tup[72], tup[93]
    cnt = sum(map(str.count, tup))
    if cnt >= a + 1 and cnt <= b - 1:
        return ""
    s = sum(range(a + 1, b - 1))
    return f'{s}'.zfill(len(str(s)))
