
import itertools

def return_binary_or_hexa(test_list):
    test_list = set(test_list)
    test_list = list(test_list)
    a, b = test_list[39], test_list[43]
    if b - a - 1 in test_list:
        return ""
    else:
        if sum(i for i in range(a + 1, b - 1) if i not in test_list) % 2:
            return format(sum(i for i in range(a + 1, b - 1) if i not in test_list), 2)
        else:
            return format(sum(i for i in range(a + 1, b - 1) if i not in test_list), 16)
