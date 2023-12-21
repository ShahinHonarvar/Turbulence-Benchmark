
def composite_nums_between_indices(numbers):
    return {number for i, number in enumerate(numbers) if 0 <= i <= 4 and is_composite_number(number)}
