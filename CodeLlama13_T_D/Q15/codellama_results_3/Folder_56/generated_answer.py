
def sum_odd_ints_inclusive(numbers):
    result = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 1:
            result += numbers[i]
    return result
