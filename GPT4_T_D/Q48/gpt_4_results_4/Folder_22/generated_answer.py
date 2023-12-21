
def return_binary_or_hexa(numbers):
    a, b = numbers[40], numbers[200]
    missing_numbers_sum = sum(set(range(a+1, b)) - set(numbers[40:201]))
    if missing_numbers_sum == 0:
        return ''
    return format(missing_numbers_sum, 'b' if missing_numbers_sum % 2 else 'X')
