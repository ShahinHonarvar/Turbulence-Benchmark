
def return_binary_or_hexa(numbers):
    a = numbers[200]
    b = numbers[202]
    missing_numbers = set(range(a + 1, b)) - set(numbers[200:202])
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2 == 0:
        return format(sum_missing_numbers, 'x')
    else:
        return format(sum_missing_numbers, 'b')
