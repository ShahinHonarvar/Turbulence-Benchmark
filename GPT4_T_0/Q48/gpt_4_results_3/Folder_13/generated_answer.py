
def return_binary_or_hexa(numbers):
    a = numbers[46]
    b = numbers[91]
    missing_numbers = set(range(a + 1, b)) - set(numbers[46:92])
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2 == 1:
        return bin(sum_missing_numbers)[2:]
    elif sum_missing_numbers % 2 == 0 and sum_missing_numbers != 0:
        return hex(sum_missing_numbers)[2:].upper()
    else:
        return ""
