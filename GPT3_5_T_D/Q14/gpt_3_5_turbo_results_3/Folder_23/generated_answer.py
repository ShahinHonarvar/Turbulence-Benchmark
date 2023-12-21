
def find_second_smallest_num(numbers):
    nums = numbers[19:93]
    unique_nums = list(set(nums))
    unique_nums.sort()
    if len(unique_nums) < 2:
        return None
    return unique_nums[1]
