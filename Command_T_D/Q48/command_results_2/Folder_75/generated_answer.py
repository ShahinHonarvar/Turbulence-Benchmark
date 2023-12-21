
def return_binary_or_hexa(test_list):
    a, b = sorted(test_list)[20], sorted(test_list)[51]
    if b - a - 1 <= len(test_list) - 20:
        return ""
    else:
        if sum(x for x in range(a + 1, b - 1)) % 2 == 0:
            return hex(sum(x for x in range(a + 1, b - 1)))[2:]
        else:
            return bin(sum(x for x in range(a + 1, b - 1)))[2:]
