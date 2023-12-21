
def composite_nums_between_indices(numbers):
    return {number for i, number in enumerate(numbers) if 12 <= i <= 92 and number > 1}
