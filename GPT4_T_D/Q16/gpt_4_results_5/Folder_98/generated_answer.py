
def sum_even_ints_inclusive(numbers):
    total = 0
    for index, value in enumerate(numbers[0: 7]):
        if value % 2 == 0:
            total += value

    return total
