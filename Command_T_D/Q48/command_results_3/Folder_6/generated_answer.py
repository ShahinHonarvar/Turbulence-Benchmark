
def return_binary_or_hexa(tup):
    a, b = tup[20], tup[93]
    cnt = a + 1
    while cnt < b:
        if tup[cnt] != -1:
            break
        cnt += 1
    if cnt == b:
        return ''
    return str(a + 1) if a + 1 == cnt else str(a + 1 + (b - 1) - cnt)
