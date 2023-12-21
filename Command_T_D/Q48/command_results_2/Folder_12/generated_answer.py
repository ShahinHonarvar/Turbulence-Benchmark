
def return_binary_or_hexa(tup):
    a, b = tup[16], tup[87]
    s = sum(x for x in range(a + 1, b - 1) if x not in tup)
    return '0b' + bin(s)[2:].zfill(len(bin(s)[2:])).decode() if s % 2 else hex(s)[2:].zfill(len(hex(s)[2:])).decode()
