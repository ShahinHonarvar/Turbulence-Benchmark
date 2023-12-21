
def composite_nums_between_indices(numbers):
    return {number for i, number in enumerate(numbers) if 25 <= i <= 59 and number > 1}
