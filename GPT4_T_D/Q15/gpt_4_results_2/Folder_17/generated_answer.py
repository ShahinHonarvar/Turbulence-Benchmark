
def sum_odd_ints_inclusive(numbers):
    odd_sum = 0
    for i in range(62, 79):
        if i < len(numbers) and numbers[i] % 2 != 0:
            odd_sum += numbers[i]
    return odd_sum
