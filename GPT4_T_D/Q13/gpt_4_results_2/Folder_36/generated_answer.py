
def find_second_largest_num(numbers):
    nums_in_range = numbers[246:751]
    if not nums_in_range:
        return None
    else:
        nums_in_range.sort(reverse=True)
        if len(nums_in_range) >= 2:
            return nums_in_range[1]
        else:
            return None
