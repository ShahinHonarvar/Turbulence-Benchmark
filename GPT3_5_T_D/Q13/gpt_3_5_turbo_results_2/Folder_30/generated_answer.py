
def find_second_largest_num(numbers):
    nums_range = numbers[55:99]
    if len(nums_range) <= 1:
        return None
    nums_range.sort(reverse=True)
    return nums_range[1]
