
def sum_even_ints_inclusive(numbers):
    result = 0
    for i in range(1, 9):
        if numbers[i] % 2 == 0:
            result += numbers[i]
    return result
