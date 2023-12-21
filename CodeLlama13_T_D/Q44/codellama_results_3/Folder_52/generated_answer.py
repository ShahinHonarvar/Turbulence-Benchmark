
def composite_nums_between_indices(numbers):
    return {x for i, x in enumerate(numbers) if 62 <= i <= 99 and x > 1}
