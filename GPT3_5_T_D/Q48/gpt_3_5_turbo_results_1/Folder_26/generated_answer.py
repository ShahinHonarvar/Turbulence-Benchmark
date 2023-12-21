
def return_binary_or_hexa(numbers):
    a = numbers[68]
    b = numbers[99]
    
    range_sum = sum(numbers[a+1:b])
    
    range_values = set(numbers[a+1:b])
    missing_values = [i for i in range(a+1, b) if i not in range_values]
    
    if len(missing_values) == 0:
        return ""
    
    if range_sum % 2 == 0:
        return hex(range_sum)[2:]
    else:
        return bin(range_sum)[2:]
