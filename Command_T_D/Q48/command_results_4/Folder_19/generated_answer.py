
def return_binary_or_hexa(test_list):
    odd_sum = 0
    for i in range(len(test_list) - 1):
        odd_sum += test_list[i + 1] - test_list[i] - 1
    if odd_sum % 2 == 1:
        return bin(odd_sum)[2:]
    else:
        return hex(odd_sum)[2:]
