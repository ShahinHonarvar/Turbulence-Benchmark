
def find_second_largest_num(numbers):
    nums = sorted(numbers[43:87])
    if len(nums) > 1:
        return nums[-2]
    else:
        return None
