
def return_binary_or_hexa(numbers):
    a = numbers[110]
    b = numbers[348]
    missing_numbers_sum = 0
    
    for i in range(a + 1, b):
        if i not in numbers[110:349]:
            missing_numbers_sum += i
    
    if missing_numbers_sum % 2 == 1:
        return bin(missing_numbers_sum)[2:]
    else:
        return hex(missing_numbers_sum)[2:].upper()
