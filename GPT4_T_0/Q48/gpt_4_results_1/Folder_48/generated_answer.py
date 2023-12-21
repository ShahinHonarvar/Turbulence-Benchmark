
def return_binary_or_hexa(numbers):
    a = numbers[933]
    b = numbers[996]
    missing_numbers = set(range(a + 1, b)) - set(numbers[933:997])
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2 == 1:
        return bin(sum_missing_numbers)[2:]
    else:
        return hex(sum_missing_numbers)[2:].upper()
