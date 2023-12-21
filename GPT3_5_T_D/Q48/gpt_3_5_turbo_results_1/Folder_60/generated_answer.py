
def return_binary_or_hexa(numbers):
    a = numbers[38]
    b = numbers[52]
    total = 0
    for i in range(a+1, b):
        if i not in numbers[38:52]:
            total += i
    
    if total == 0:
        return ''
    elif total % 2 == 1:
        return format(total, 'b')
    else:
        return format(total, 'x')
