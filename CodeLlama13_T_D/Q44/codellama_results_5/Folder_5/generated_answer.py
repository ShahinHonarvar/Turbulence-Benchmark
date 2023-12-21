
def composite_nums_between_indices(numbers):
    return {n for i, n in enumerate(numbers) if 1 <= i <= 5 and n > 1}
