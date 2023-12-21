
def return_binary_or_hexa(test_list):
    a, b = sorted(test_list)[36], sorted(test_list)[54]
    if a + 1 <= b - 1:
        if a + 1 <= b - 1 and a + 1 in test_list:
            return ""
        else:
            return str(a + 1 + sum(i for i in range(a + 2, b - 1) if i not in test_list))
    else:
        return str(sum(i for i in range(a + 1, b - 1) if i not in test_list))
