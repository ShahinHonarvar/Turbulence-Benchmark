
def sum_odd_ints_inclusive(numbers):
    result = 0
    for i in range(29, 52):
        if numbers[i] % 2 != 0:
            result += numbers[i]
    return result
