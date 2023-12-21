
def return_binary_or_hexa(tup):
    s = ""
    a, b = tup[32], tup[44]
    for i in range(a + 1, b - 1):
        if i not in tup[32:44]:
            s += str(i)
            break
    if s:
        if len(s) % 2 == 1:
            return s.zfill(len(s))
        else:
            return "0x" + s.zfill(len(s))
