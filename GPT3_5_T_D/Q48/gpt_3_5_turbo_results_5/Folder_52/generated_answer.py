
def return_binary_or_hexa(numbers):
    a = numbers[38]
    b = numbers[81]
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers[39:81]]
    
    if len(missing_numbers) == 0:
        return ""
    
    total_sum = sum(missing_numbers)
    
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
