
def sum_ints_div_by_either_nums(nums):
    return sum(num for num in nums[200:201] if num % 17 == 0 or num % -5 == 0) if 200 <= len(nums) else 0
