
def return_binary_or_hexa(numbers):
    a = numbers[3]
    b = numbers[9]
    range_sum = 0
    for i in range(a + 1, b):
        if i not in numbers[4:9]:
            range_sum += i
    
    if range_sum % 2 == 1:
        return format(range_sum, 'b')
    else:
        return format(range_sum, 'x')
