
def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[281:695]:
        if num % -722 == 0 or num % -731 == 0:
            total += num
    return total
