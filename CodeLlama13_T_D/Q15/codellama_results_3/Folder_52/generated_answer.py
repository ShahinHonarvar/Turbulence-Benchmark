
def sum_odd_ints_inclusive(numbers):
    result = 0
    for i in range(28, 39):
        if numbers[i] % 2 == 1:
            result += numbers[i]
    return result
