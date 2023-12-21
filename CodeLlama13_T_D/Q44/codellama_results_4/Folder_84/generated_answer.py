
def composite_nums_between_indices(numbers):
    indices = range(30, 49)
    return {n for i, n in enumerate(numbers) if i in indices and n > 1}
