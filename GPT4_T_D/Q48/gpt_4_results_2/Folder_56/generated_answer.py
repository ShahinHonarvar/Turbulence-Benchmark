
def return_binary_or_hexa(numbers):
    a = numbers[7]
    b = numbers[9]
    
    sum_val = sum(set(range(a + 1, b)) - set(numbers[7:10]))
    
    if sum_val % 2 != 0:
        return bin(sum_val)[2:]
    elif sum_val == 0:
        return ''
    else:
        return hex(sum_val)[2:].upper()
