
def return_binary_or_hexa(tup):
    a, b = tup[70], tup[98]
    if a + 1 <= b - 1:
        res = (b - a - 1) % 2
    else:
        res = (b - a - 1) // 2
    if res:
        return f"0b{res}"
    else:
        return f"0x{res:02x}"
