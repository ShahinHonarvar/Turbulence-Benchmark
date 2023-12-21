
def composite_nums_between_indices(numbers):
    return {number for i, number in enumerate(numbers) if 20 <= i <= 30 and number > 1}
