
def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[89]
    missing_numbers = set(range(a + 1, b)) - set(numbers[86:90])
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2 == 1:
        return bin(sum_missing_numbers)[2:]
    else:
        return hex(sum_missing_numbers)[2:].upper()
