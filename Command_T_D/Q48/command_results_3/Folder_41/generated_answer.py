
def return_binary_or_hexa(test_list):
    res = ""
    a, b = sorted(test_list)[3], sorted(test_list)[8]
    if a == b:
        return ""
    s = sum(x for x in range(a + 1, b - 1) if x not in test_list)
    if s % 2 == 0:
        return hex(s)
    else:
        return bin(s)
