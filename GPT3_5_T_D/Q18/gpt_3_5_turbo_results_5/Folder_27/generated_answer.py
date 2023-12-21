
def sum_ints_div_by_either_nums(nums):
    div_nums = [-36, -89]
    total = 0
    for num in nums[20:36+1]:
        if num % div_nums[0] == 0 or num % div_nums[1] == 0:
            total += num
    return total
