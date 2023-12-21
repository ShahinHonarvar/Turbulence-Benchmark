
def find_second_smallest_num(nums):
    first_three_nums = nums[:3]

    if len(first_three_nums) < 2:
        return None

    first_three_nums.sort()

    return first_three_nums[1]
