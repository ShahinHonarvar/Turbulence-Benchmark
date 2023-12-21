
def return_binary_or_hexa(numbers):
    a = numbers[33]
    b = numbers[78]
    range_sum = sum(numbers[a+1:b])
    missing_numbers = set(range(a+1, b+1)) - set(numbers[a:b+1])
    
    if len(missing_numbers) == 0:
        return ""
    elif range_sum % 2 == 1:
        return bin(range_sum)[2:]
    else:
        return hex(range_sum)[2:]
