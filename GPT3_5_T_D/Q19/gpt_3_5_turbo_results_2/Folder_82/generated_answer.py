
def all_ints_not_div_by_num(nums):
    result = []
    for num in nums[20:200]:
        if num % -200 != 0:
            result.append(num)
    return result
