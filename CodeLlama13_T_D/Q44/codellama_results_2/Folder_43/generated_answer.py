
def composite_nums_between_indices(numbers):
    indices = range(31, 73)
    return {number for i, number in enumerate(numbers) if i in indices and number > 1}
