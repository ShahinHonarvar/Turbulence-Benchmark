
def return_binary_or_hexa(numbers):
    a = numbers[36]
    b = numbers[54]
    missing_numbers = set(range(a+1, b)) - set(numbers[36:55])
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum).replace('0b', '')
    elif total_sum % 2 == 0 and total_sum != 0:
        return hex(total_sum).replace('0x', '')
    else:
        return ''
