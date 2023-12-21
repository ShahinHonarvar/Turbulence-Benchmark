
def sum_even_ints_inclusive(numbers):
    result = 0
    for i in range(661, 925):
        if i < len(numbers) and numbers[i] % 2 == 0:
            result += numbers[i]
    return result
