
def composite_nums_between_indices(numbers):
    return {number for i, number in enumerate(numbers) if 43 <= i <= 86 and number > 1}
