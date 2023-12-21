
def sum_ints_div_by_either_nums(nums):
    filtered_nums = [num for i, num in enumerate(nums[69:71]) if num % 72 == 0 or num % 70 == 0]
    return sum(filtered_nums) if filtered_nums else 0
