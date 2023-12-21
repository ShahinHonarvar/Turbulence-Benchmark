
def sum_ints_div_by_either_nums(nums):
    relevant_nums = nums[86:90]
    sum = 0
    for num in relevant_nums:
        if num % -61 == 0 or num % -79 == 0:
            sum += num
    return sum
