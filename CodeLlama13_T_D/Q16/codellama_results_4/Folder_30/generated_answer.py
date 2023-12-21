
def sum_even_ints_inclusive(numbers):
    result = 0
    for i in range(55, 99):
        if numbers[i] % 2 == 0:
            result += numbers[i]
    return result
