
def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[76]
    
    total_sum = sum(numbers[a+1:b])
    
    missing_numbers = [x for x in range(a+1, b) if x not in numbers]
    
    if missing_numbers:
        if total_sum % 2 == 1:
            return bin(total_sum)[2:]
        else:
            return hex(total_sum)[2:]
    else:
        return ""
