
def all_ints_div_by_both_two_nums(nums):
    result = []
    for num in nums[50:200]:
        if num % -34 == 0 and num % 64 == 0:
            result.append(num)
    return result
