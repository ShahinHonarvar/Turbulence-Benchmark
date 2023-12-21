
def composite_nums_between_indices(numbers):
    return {number for i, number in enumerate(numbers) if 22 <= i <= 50 and number != 1}
