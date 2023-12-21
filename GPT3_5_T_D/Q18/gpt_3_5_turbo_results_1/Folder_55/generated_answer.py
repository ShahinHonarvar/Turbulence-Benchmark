
def sum_ints_div_by_either_nums(nums):
    return sum([num for num in nums[:10] if num % 10 == 0 or num % 100 == 0])
