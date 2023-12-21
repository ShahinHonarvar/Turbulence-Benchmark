
def sum_ints_div_by_either_nums(nums):
    sum = 0
    for num in nums[:3]:
        if num % -2 == 0 or num % 3 == 0:
            sum += num
    return sum
