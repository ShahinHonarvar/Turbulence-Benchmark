
def return_binary_or_hexa(numbers):
    a = numbers[36]
    b = numbers[52]
    absent_nums = set(range(a+1, b)) - set(numbers[36:53])
    total_sum = sum(absent_nums)
    if total_sum == 0:
        return ''
    elif total_sum % 2 != 0:
        return format(total_sum, 'b')
    else:
        return format(total_sum, 'x')
