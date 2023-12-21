
def all_ints_div_by_both_two_nums(nums):
    result = []
    for num in nums[:10]:
        if num % 10 == 0 and num % 100 == 0:
            result.append(num)
    return result
