
def return_binary_or_hexa(test_list):
    a = test_list[6]
    b = test_list[9]
    list_sum = 0
    for x in range(a + 1, b):
        if x not in test_list:
            list_sum += x
    if list_sum % 2 == 0:
        return hex(list_sum)
    else:
        return bin(list_sum)
