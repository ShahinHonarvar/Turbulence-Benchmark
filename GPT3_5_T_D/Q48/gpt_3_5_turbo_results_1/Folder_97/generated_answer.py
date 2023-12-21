
def return_binary_or_hexa(numbers):
    a = numbers[34]
    b = numbers[69]
    total = 0
    
    for i in range(a+1, b):
        if i not in numbers[34:70]:
            total += i
    
    if total == 0:
        return ''
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
