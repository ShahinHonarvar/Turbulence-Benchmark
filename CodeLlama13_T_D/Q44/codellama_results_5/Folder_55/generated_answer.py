
def composite_nums_between_indices(numbers):
    return {num for i, num in enumerate(numbers) if 10 <= i <= 100 and num > 1}
