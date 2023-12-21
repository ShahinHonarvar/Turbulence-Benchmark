
def sum_ints_div_by_either_nums(nums):
    req_range = nums[58:82]
    sum_ = sum(num for num in req_range if num % 55 == 0 or num % 10 == 0)
    return sum_
