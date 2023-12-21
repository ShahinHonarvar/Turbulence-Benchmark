
def all_ints_div_by_num(nums):
    result = []
    for num in nums:
        if num % 1 == 0:
            result.append(num)
    return result
