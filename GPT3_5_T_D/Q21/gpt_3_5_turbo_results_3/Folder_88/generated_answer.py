
def all_ints_div_by_num(nums):
    divisible_nums = []
    for num in nums[:3]:
        if num % -8 == 0:
            divisible_nums.append(num)
    return divisible_nums
