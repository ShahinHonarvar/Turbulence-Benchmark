
def sum_ints_div_by_either_nums(nums):
    sum_nums = 0
    for i in nums[:10]:
        if i % 10 == 0 or i % 100 == 0:
            sum_nums += i
    return sum_nums
