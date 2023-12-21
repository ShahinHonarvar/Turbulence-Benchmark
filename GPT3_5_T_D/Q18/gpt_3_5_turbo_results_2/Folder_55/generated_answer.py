
def sum_ints_div_by_either_nums(nums):
    nums_subset = nums[:10]
    result = 0
    for num in nums_subset:
        if num % 10 == 0 or num % 100 == 0:
            result += num
    return result
