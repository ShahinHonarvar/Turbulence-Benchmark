
def return_binary_or_hexa(numbers):
    a = numbers[45]
    b = numbers[48]
    missing_numbers = set(range(a + 1, b)) - set(numbers[45:49])
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2 == 1:
        return bin(sum_missing_numbers)[2:]
    else:
        return hex(sum_missing_numbers)[2:].upper()
