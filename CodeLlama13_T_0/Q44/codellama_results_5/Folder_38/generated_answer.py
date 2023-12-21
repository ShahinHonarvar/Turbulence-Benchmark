
def composite_nums_between_indices(numbers):
    return {number for i, number in enumerate(numbers) if 29 <= i <= 93 and number > 1}
