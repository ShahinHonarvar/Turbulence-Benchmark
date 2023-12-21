
def return_binary_or_hexa(numbers):
    a = numbers[37]
    b = numbers[43]
    missing_numbers = set(range(a + 1, b)) - set(numbers[37:44])
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2 == 1:
        return bin(sum_missing_numbers)[2:]
    elif sum_missing_numbers % 2 == 0 and sum_missing_numbers != 0:
        return hex(sum_missing_numbers)[2:].upper()
    else:
        return ""
