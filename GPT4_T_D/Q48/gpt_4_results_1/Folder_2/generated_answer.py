
def return_binary_or_hexa(numbers):
    a = numbers[72]
    b = numbers[93]
    missing_numbers = set(range(a + 1, b)) - set(numbers[72:94])
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2 == 0:
        return hex(sum_missing_numbers)[2:].upper()
    else:
        return bin(sum_missing_numbers)[2:]
