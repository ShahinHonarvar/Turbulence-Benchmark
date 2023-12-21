
def return_binary_or_hexa(test_list):
    a, b = test_list[13], test_list[91]
    test_list = set(test_list)
    if a + 1 <= b - 1:
        value = (b - a - 1) & 1
        if value:
            return format(sum(x for x in range(a + 1, b) if x not in test_list), "b")
        else:
            return format(sum(x for x in range(a + 1, b) if x not in test_list), "x")
    else:
        return ""
