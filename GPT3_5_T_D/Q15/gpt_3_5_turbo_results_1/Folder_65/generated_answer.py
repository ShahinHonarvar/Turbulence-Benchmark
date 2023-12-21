
def sum_odd_ints_inclusive(numbers):
    sum = 0
    for i in range(56, 99):
        if numbers[i] % 2 != 0:
            sum += numbers[i]
    return sum
