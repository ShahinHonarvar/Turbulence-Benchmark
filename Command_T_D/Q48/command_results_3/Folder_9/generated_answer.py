
def return_binary_or_hexa(tup):
    if len(tup) == 0:
        return ""
    a = tup[70]
    b = tup[200]
    if a + 1 <= b - 1:
        diff = b - a - 1
        if a % 2 == 1:
            return "0b" + bin(diff)
        else:
            return "0x" + hex(diff)
    else:
        return ""
