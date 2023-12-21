
def composite_nums_between_indices(numbers):
    if not numbers:
        return set()
    return {num for i, num in enumerate(numbers) if 19 <= i <= 92 and num > 1}
