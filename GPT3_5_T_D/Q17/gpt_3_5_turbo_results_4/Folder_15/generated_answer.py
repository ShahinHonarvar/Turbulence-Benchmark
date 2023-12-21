
def all_ints_div_by_both_two_nums(nums):
    result = []
    for num in nums[:3]:
        if num % -2 == 0 and num % 3 == 0:
            result.append(num)
    return result
