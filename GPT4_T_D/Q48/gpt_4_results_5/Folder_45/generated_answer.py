
def return_binary_or_hexa(numbers):
    a = numbers[30]
    b = numbers[200]

    missing_sum = sum(set(range(a + 1, b)) - set(numbers[30:201]))

    if missing_sum == 0:
        return ''
    
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    
    else:
        return hex(missing_sum)[2:]
