
def return_binary_or_hexa(numbers):
    a = numbers[6]
    b = numbers[9]
    missing_numbers = set(range(a + 1, b)) - set(numbers[6:10])
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2 == 1:
        return bin(sum_missing_numbers)[2:]
    else:
        return hex(sum_missing_numbers)[2:].upper()
