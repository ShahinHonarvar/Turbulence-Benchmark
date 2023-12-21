
def return_binary_or_hexa(test_tup):
    a, b = test_tup[50], test_tup[200]
    val = b - a - 1
    if val % 2 == 0:
        return hex(val)
    else:
        return f"0b{val:b}"
