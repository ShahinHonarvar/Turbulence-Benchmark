
def composite_nums_between_indices(numbers):
    return {number for i, number in enumerate(numbers) if 80 <= i <= 200 and number > 1}
