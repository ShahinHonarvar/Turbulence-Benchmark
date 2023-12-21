
def composite_nums_between_indices(numbers):
    return {number for i, number in enumerate(numbers) if 19 <= i <= 92 and number > 1}
