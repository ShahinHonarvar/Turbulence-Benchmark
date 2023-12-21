
def sum_odd_ints_inclusive(numbers):
    total = 0

    for i in range(56, 58):
        if i < len(numbers) and numbers[i] % 2 != 0:
            total += numbers[i]

    return total
