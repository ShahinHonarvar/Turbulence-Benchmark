
def sum_ints_div_by_either_nums(nums):
    range_sum = 0
    for num in nums[28:97+1]:
        if num % 90 == 0 or num % 97 == 0:
            range_sum += num
    return range_sum
