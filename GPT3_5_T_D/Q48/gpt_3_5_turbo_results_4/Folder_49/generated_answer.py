
def return_binary_or_hexa(numbers):
    a = numbers[80]
    b = numbers[200]
    total = sum(numbers[a+1:b])
    missing_numbers = set(range(a+1, b)) - set(numbers[a+1:b])
    
    if len(missing_numbers) == 0:
        return ""
    
    if total % 2 == 1:
        return format(total, 'b')
    else:
        return format(total, 'X')
