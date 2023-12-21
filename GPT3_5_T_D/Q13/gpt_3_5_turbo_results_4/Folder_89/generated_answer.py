
def find_second_largest_num(numbers):
    if len(numbers) < 83:
        return None
    nums_subset = numbers[56:83]
    nums_subset.sort(reverse=True)
    return nums_subset[1] if len(nums_subset) > 1 else None
