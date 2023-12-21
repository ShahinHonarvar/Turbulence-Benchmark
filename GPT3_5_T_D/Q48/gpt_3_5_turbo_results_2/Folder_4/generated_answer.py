
def return_binary_or_hexa(numbers):
    a = numbers[49]
    b = numbers[74]
    total_sum = sum(range(a + 1, b))
    missing_numbers = [x for x in range(a + 1, b) if x not in numbers[50:74]]
    
    if not missing_numbers:
        return ''
    
    if total_sum % 2 == 1:
        binary_sum = bin(total_sum)[2:]
        return binary_sum
    else:
        hexa_sum = hex(total_sum)[2:]
        return hexa_sum
