
def return_binary_or_hexa(numbers):
    a = numbers[42]
    b = numbers[87]
    not_in_tuple = set(range(a + 1, b)) - set(numbers[42:87])
    sum_not_in_tuple = sum(not_in_tuple)
    if sum_not_in_tuple == 0:
        return ""
    elif sum_not_in_tuple % 2 == 0:
        return hex(sum_not_in_tuple)[2:]
    else:
        return bin(sum_not_in_tuple)[2:]
