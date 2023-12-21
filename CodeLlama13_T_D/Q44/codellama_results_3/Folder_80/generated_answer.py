
def composite_nums_between_indices(numbers):
    return {x for i, x in enumerate(numbers) if 62 <= i <= 78 and len(str(x)) > 1}
