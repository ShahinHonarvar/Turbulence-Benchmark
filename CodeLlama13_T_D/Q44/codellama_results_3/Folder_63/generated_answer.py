
def composite_nums_between_indices(numbers):
    return {number for index, number in enumerate(numbers) if 17 <= index <= 78 and number > 1}
