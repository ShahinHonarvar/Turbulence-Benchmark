
def composite_nums_between_indices(numbers):
    return {number for i, number in enumerate(numbers) if 28 <= i <= 40 and number > 1}
