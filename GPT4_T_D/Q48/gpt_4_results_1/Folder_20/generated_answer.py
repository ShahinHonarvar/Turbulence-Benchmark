
def return_binary_or_hexa(numbers):
    a = numbers[27]
    b = numbers[96]
    total = sum(set(range(a+1,b)).difference(numbers[27:97]))
    
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()
