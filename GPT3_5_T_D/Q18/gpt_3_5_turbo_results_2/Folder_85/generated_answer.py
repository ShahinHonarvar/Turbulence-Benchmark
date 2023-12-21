
def sum_ints_div_by_either_nums(nums):
    sum_val = 0
    for num in nums[1:9]:
        if num % -9 == 0 or num % -3 == 0:
            sum_val += num
    return sum_val
