
def return_binary_or_hexa(numbers):
    a, b = numbers[0], numbers[10]
    missing_nums_sum = sum(set(range(a + 1, b)) - set(numbers[1:10]))
    
    if missing_nums_sum % 2 != 0:
        return bin(missing_nums_sum)[2:]
    elif missing_nums_sum % 2 == 0 and missing_nums_sum != 0:
        return hex(missing_nums_sum)[2:].upper()
    else:
        return ""
