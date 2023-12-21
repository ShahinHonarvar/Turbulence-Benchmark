
def return_binary_or_hexa(test_list):
    test_sum = 0
    for i in range(len(test_list)):
        if test_list[i] != i + 1:
            test_sum += i + 1
            break
    if test_sum % 2 == 1:
        return bin(test_sum).zfill(8)
    else:
        return hex(test_sum).zfill(8)
