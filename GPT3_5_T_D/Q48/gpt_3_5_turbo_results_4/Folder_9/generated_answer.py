
def return_binary_or_hexa(numbers):
    a = numbers[70]
    b = numbers[200]
    total_sum = sum(numbers[a+1:b])
    
    if all(i in numbers[a:b+1] for i in range(a+1, b)):
        return ""
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]
