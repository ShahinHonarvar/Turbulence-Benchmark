
def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[35]
    total_sum = sum(numbers[a+1:b])
    missing_numbers = set(range(a+1, b)) - set(numbers[a+1:b])
    
    if len(missing_numbers) == 0:
        return ""
    
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
