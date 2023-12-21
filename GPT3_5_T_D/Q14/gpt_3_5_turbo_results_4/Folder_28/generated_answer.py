
def find_second_smallest_num(numbers):
    nums = numbers[22:51]
    if len(nums) < 2:
        return None
    sort_nums = sorted(set(nums))
    return sort_nums[1]
