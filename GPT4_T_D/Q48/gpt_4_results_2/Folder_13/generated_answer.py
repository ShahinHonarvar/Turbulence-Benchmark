
def return_binary_or_hexa(numbers):
    a = numbers[46]
    b = numbers[91]
    missing_numbers = [x for x in range(a + 1, b) if x not in numbers[46:92]]
    sum_missing_numbers = sum(missing_numbers)
    
    if len(missing_numbers) == 0:
        return ''
    elif sum_missing_numbers % 2 == 0:
        return hex(sum_missing_numbers)[2:].upper()
    else:
        return bin(sum_missing_numbers)[2:]
