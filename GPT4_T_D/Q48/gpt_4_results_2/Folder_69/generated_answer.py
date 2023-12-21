
def return_binary_or_hexa(numbers):
    a = numbers[39]
    b = numbers[43]
    missing_numbers = set(range(a + 1, b)) - set(numbers[39:44])
    sum_nums = sum(missing_numbers)
    
    if sum_nums == 0:
        return ''
    elif sum_nums % 2 == 0:
        return hex(sum_nums)[2:]
    else:
        return bin(sum_nums)[2:]
