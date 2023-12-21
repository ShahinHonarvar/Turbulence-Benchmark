
def return_binary_or_hexa(numbers):
    a = numbers[56]
    b = numbers[90]
    total_sum = 0
    for i in range(a + 1, b):
        if i not in numbers[56:91]:
            total_sum += i

    if total_sum % 2 == 0:
        return format(total_sum, 'X')
    else:
        return format(total_sum, 'b')
