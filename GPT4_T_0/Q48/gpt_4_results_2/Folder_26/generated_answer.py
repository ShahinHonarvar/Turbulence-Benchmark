
def return_binary_or_hexa(numbers):
    a = numbers[68]
    b = numbers[99]
    missing_numbers = set(range(a + 1, b)) - set(numbers[68:100])
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2 == 1:
        return bin(sum_missing_numbers)[2:]
    else:
        return hex(sum_missing_numbers)[2:].upper()
