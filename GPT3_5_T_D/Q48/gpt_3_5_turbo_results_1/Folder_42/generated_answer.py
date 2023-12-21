
def return_binary_or_hexa(numbers):
    a = numbers[18]
    b = numbers[60]
    subset = set(numbers[19:60])
    
    result = 0
    for num in range(a+1, b):
        if num not in subset:
            result += num
            
    if result == 0:
        return ""
    elif result % 2 == 1:
        return bin(result)[2:]
    else:
        return hex(result)[2:]
