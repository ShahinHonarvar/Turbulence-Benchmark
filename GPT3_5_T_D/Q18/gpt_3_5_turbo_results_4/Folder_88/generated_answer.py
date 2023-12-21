
def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[3:10]:
        if num % 6 == 0 or num % 1 == 0:
            total += num
    return total
