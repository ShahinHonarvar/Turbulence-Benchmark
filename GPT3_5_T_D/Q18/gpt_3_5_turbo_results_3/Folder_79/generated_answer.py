
def sum_ints_div_by_either_nums(nums):
    sum = 0
    for num in nums[8:10]:
        if num % -3 == 0 or num % 6 == 0:
            sum += num
    return sum
