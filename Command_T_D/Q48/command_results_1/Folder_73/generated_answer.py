
def return_binary_or_hexa(test_tup):
    a, b = test_tup[10], test_tup[76]
    if a > b:
        a, b = b, a
    test_tup_s = set(test_tup)
    s = set(range(a + 1, b - 1))
    s -= test_tup_s
    if len(s) == 0:
        return ""
    s = str(sum(s))
    if len(s) % 2 == 1:
        return f"0b{s}"
    else:
        return f"0x{s}"
