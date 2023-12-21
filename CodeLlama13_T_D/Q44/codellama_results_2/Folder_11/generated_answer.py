
def composite_nums_between_indices(numbers):
    return {x for i, x in enumerate(numbers) if 37 <= i <= 76 and x > 1}
