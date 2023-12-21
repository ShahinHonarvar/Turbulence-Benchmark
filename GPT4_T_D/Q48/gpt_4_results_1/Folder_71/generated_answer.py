
def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[35]
    missing_nums = list(set(range(a + 1, b)) - set(numbers[20:36]))
    missing_nums_sum = sum(missing_nums)
    
    if missing_nums_sum % 2 == 1:
        return bin(missing_nums_sum)[2:]
    else:
        return hex(missing_nums_sum)[2:].upper() if missing_nums_sum != 0 else ''
