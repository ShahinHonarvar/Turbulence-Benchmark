
def composite_nums_between_indices(numbers):
    return {n for i, n in enumerate(numbers) if 27 <= i <= 55 and n > 1}
