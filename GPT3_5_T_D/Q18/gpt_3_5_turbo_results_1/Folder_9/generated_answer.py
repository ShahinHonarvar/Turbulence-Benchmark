
def sum_ints_div_by_either_nums(nums):
    return sum(num for num in nums[70:201] if num % 3 == 0 or num % -300 == 0)
