
def all_ints_div_by_num(nums):
    divisible_by_9 = [num for num in nums[:3] if num % 9 == 0]
    return divisible_by_9
