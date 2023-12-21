
def composite_nums_between_indices(numbers):
    return {number for i, number in enumerate(numbers) if 70 <= i <= 84 and number > 1}
