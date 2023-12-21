
def return_binary_or_hexa(test_tup):
    test_tup = sorted(test_tup)
    a, b = test_tup[90], test_tup[200]
    if b - a - 1 <= 0:
        return ""
    test_tup_num_sum = 0
    for i in range(a + 1, b - 1):
        if i not in test_tup:
            test_tup_num_sum += i
    if test_tup_num_sum % 2 == 0:
        return hex(test_tup_num_sum)
    else:
        return "0b" + bin(test_tup_num_sum).zfill(len(str(test_tup_num_sum))).lower()
