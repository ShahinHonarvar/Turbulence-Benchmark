
def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[100]
    missing_numbers = set(range(a + 1, b)) - set(numbers[10:101])
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2 == 0:
        return hex(sum_missing_numbers)[2:]
    else:
        return bin(sum_missing_numbers)[2:]
