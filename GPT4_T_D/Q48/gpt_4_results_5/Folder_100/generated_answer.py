
def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[78]
    sum_absent = sum(set(range(a+1, b)) - set(numbers[44:78]))
    
    if sum_absent == 0:
        return ''
    
    elif sum_absent % 2 == 0:
        return hex(sum_absent)[2:].upper()
        
    else:
        return bin(sum_absent)[2:]
