
def return_binary_or_hexa(test_tup):
    s = sum(range(test_tup[70] + 1, test_tup[200] - 1))
    if s % 2 == 0:
        return hex(s)
    else:
        return f"0b{s:b}"
