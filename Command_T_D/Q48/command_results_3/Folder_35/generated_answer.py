
import binary as bin

def return_binary_or_hexa(tup):
    a, b = tup[77], tup[84]
    if a == b:
        return ""
    sm = sum(x for x in range(a + 1, b))
    if sm % 2 == 0:
        return hex(sm)
    else:
        return bin(sm)
