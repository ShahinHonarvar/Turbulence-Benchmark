
def find_second_largest_num(numbers):
    nums_range = numbers[12:93]
    if len(nums_range) < 2:
        return None
    nums_range.sort(reverse=True)
    return nums_range[1]
