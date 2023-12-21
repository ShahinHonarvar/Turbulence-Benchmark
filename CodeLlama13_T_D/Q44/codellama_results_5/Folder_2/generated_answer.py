
def composite_nums_between_indices(numbers):
    return {n for i, n in enumerate(numbers) if 35 <= i <= 49 and n > 1}
