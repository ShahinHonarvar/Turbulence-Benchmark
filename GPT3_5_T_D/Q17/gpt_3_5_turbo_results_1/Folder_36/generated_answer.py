
def all_ints_div_by_both_two_nums(nums):
    divisible_nums = []
    
    for num in nums[299:383]:
        if num % 858 == 0 and num % 952 == 0:
            divisible_nums.append(num)
    
    return divisible_nums
