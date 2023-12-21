
def return_binary_or_hexa(numbers):
    a = numbers[32]
    b = numbers[44]
    missing_sum = sum([x for x in range(a + 1, b) if x not in numbers[32:45]])
    
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]
