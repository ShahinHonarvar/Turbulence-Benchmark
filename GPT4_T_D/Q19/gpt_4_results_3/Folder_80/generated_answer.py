
def all_ints_not_div_by_num(nums):
    result = []
    for num in nums[16:20]:
        if num % 93 != 0:
            result.append(num)
    return result
