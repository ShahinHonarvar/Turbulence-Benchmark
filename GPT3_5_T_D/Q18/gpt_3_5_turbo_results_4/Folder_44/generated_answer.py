
def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[25:71]:
        if num % 74 == 0 or num % 15 == 0:
            total += num
    return total
