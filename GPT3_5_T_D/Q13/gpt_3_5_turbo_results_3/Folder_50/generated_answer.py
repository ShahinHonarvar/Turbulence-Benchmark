
def find_second_largest_num(numbers):
    nums_range = numbers[70:85]
    if len(nums_range) < 2:
        return None
    nums_range.sort()
    return nums_range[-2]
