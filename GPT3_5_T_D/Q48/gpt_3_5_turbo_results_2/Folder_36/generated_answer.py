
def return_binary_or_hexa(numbers):
    a = numbers[110]
    b = numbers[348]
    total = 0
    missing_numbers = []
    
    for i in range(a+1, b):
        if i not in numbers[110:349]:
            total += i
            missing_numbers.append(i)
    
    if len(missing_numbers) == 0:
        return ""
    elif total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]
