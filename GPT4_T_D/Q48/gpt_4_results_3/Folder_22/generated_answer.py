
def return_binary_or_hexa(numbers):
    a = numbers[40]
    b = numbers[200]
    total = sum(set(range(a+1, b)) - set(numbers[40:200+1]))
    
    if total == 0:
        return ""
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()
