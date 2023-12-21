
def composite_nums_between_indices(numbers):
    return {n for i, n in enumerate(numbers) if 0 <= i < 3 and n > 1}
