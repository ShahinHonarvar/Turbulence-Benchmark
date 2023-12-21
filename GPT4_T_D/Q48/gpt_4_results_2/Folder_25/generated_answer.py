
def return_binary_or_hexa(numbers_tuple):
    a = numbers_tuple[37]
    b = numbers_tuple[43]
    missing_numbers = set(range(a+1, b)) - set(numbers_tuple[37:44])
    num_sum = sum(missing_numbers)
    if num_sum % 2 == 1:
        return bin(num_sum)[2:]
    elif num_sum % 2 == 0:
        return hex(num_sum)[2:].upper()
    else:
        return ""
