
def return_binary_or_hexa(numbers):
    a = numbers[6]
    b = numbers[9]
    excluded_nums = numbers[7:9]
    
    sum = 0
    for i in range(a + 1, b):
        if i not in excluded_nums and i not in numbers:
            sum += i
    
    if sum == 0:
        return ""
    elif sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
