
def return_binary_or_hexa(numbers):
    a = numbers[77]
    b = numbers[84]
    total_sum = 0
    for i in range(a+1, b):
        if i not in numbers[77:85]:
            total_sum += i
    
    if total_sum == 0:
        return ""
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]
