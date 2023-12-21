
def composite_nums_between_indices(numbers):
    return {n for i, n in enumerate(numbers) if 10 <= i <= 100 and n > 1}
