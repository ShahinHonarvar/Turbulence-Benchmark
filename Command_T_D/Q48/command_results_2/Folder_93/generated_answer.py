
def return_binary_or_hexa(tup):
    i = tup.index(a)
    j = tup.index(b)
    cnt = b - a - 1
    if cnt % 2 == 1:
        return bin(cnt)
    else:
        return hex(cnt)
