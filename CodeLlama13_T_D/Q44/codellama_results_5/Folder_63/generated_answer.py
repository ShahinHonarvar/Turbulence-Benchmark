
def composite_nums_between_indices(numbers):
    indices = range(17, 79)
    return set(filter(lambda x: x > 1 and all(x % y for y in range(2, int(x ** 0.5) + 1)), numbers))
