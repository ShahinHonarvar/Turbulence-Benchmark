
def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[70]
    missing_numbers = set(range(a + 1, b)) - set(numbers[13:70])

    if len(missing_numbers) == 0:
        return ""
        
    total = sum(missing_numbers)
    
    return bin(total)[2:] if total % 2 != 0 else hex(total)[2:].upper()
