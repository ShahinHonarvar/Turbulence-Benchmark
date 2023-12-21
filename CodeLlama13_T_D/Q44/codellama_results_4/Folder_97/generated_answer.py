
def composite_nums_between_indices(numbers):
    return {x for i, x in enumerate(numbers) if i >= 15 and i <= 39 and x > 1}
