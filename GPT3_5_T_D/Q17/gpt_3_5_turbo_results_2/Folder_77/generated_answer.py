 
def all_ints_div_by_both_two_nums(nums):
    result = []
    for num in nums[828:933]:
        if num % -649 == 0 and num % -461 == 0:
            result.append(num)
    return result
