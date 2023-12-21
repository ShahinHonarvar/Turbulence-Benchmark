
def return_binary_or_hexa(numbers):
    a = numbers[19]
    b = numbers[32]
    sum_ = sum(set(range(a + 1, b)) - set(numbers[19:33]))
    if sum_ % 2 == 0:
        return format(sum_, 'x')
    else:
        return format(sum_, 'b')
