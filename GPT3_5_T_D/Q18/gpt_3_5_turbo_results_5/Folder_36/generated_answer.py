
def sum_ints_div_by_either_nums(nums):
    sum = 0
    for num in nums[299:383]:
        if num % 858 == 0 or num % 952 == 0:
            sum += num
    return sum
