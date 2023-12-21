
def return_binary_or_hexa(numbers):
    a = numbers[46]
    b = numbers[91]
    missing_nums = set(range(a + 1, b)) - set(numbers[46:92])
    num_sum = sum(missing_nums)
    
    if num_sum == 0:
        return ''
    elif num_sum % 2 == 1:
        return bin(num_sum)[2:]
    else:
        return hex(num_sum)[2:].upper()
