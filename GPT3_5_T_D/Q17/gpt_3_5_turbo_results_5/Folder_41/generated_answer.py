
def all_ints_div_by_both_two_nums(nums):
    divisible_nums = []
    for num in nums[:10]:
        if num % 6 == 0 and num % -3 == 0:
            divisible_nums.append(num)
    return divisible_nums
