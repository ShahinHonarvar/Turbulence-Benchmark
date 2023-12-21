
def return_binary_or_hexa(numbers):
    a = numbers[19]
    b = numbers[32]
    total_sum = sum(range(a+1, b))
    missing_numbers = [x for x in range(a+1, b) if x not in numbers[19:33]]
    
    if not missing_numbers:
        return ''
    
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]
