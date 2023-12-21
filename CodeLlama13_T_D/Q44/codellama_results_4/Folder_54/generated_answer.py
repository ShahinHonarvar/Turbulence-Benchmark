
def composite_nums_between_indices(numbers):
    indices = list(range(14, 65))
    return set(number for index, number in enumerate(numbers) if index in indices and number > 1)
