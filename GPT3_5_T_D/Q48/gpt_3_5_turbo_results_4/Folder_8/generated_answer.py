
def return_binary_or_hexa(numbers):
    a = numbers[45]
    b = numbers[48]
    excluded_numbers = set(numbers[45:49])
    total = sum(x for x in range(a+1, b) if x not in excluded_numbers)
    
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()
