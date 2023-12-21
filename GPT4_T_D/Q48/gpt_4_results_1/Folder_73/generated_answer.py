
def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[76]
    subset = numbers[10:77]
    numbers_not_in_subset = set(range(a + 1, b)) - set(subset)
    sum_numbers_not_subset = sum(numbers_not_in_subset)
    if sum_numbers_not_subset == 0:
        return ''
    elif sum_numbers_not_subset % 2 == 0:
        return hex(sum_numbers_not_subset)[2:]
    else:
        return bin(sum_numbers_not_subset)[2:]
