
def sum_even_ints_inclusive(numbers):
    sliced = numbers[37:52]
    return sum(num for num in sliced if num % 2 == 0)
