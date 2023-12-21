
def all_ints_div_by_both_two_nums(nums):
    start_idx = 86
    end_idx = 90
    result = []
    for num in nums[start_idx:end_idx+1]:
        if num % -71 == 0 and num % -67 == 0:
            result.append(num)
    return result
