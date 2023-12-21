
def composite_nums_between_indices(numbers):
    return {number for i, number in enumerate(numbers) if 75 <= i <= 94 and number > 1}
