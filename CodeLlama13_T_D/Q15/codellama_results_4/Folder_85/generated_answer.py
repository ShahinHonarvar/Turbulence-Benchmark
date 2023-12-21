
def sum_odd_ints_inclusive(numbers):
    odd_ints = []
    for i in range(6, 9):
        if numbers[i] % 2 != 0:
            odd_ints.append(numbers[i])
    return sum(odd_ints)
