
def return_binary_or_hexa(numbers):
    a = numbers[38]
    b = numbers[52]
    missing_numbers = set(range(a + 1, b)) - set(numbers[38:53])
    sum_numbers = sum(missing_numbers)
    if sum_numbers % 2 == 1:
        return bin(sum_numbers)[2:]
    else:
        return hex(sum_numbers)[2:].upper()
