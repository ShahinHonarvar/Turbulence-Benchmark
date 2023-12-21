
def sum_odd_ints_inclusive(numbers):
    return sum(num for ind, num in enumerate(numbers[310:371]) if num % 2 != 0)
