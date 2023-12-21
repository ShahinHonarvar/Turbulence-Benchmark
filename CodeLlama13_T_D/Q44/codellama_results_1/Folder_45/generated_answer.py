
def composite_nums_between_indices(numbers):
    return {x for i, x in enumerate(numbers) if 40 <= i <= 200 and x > 1}
