 
def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[35]
    total = sum(numbers[a+1:b])
    missing_numbers = [x for x in range(a+1, b) if x not in numbers]
    if missing_numbers:
        binary = bin(total)[2:]
        hexadecimal = hex(total)[2:]
        return binary if total % 2 == 1 else hexadecimal.upper()
    return ""
