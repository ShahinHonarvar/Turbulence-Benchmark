
def if_perfect_num(nums):
    if len(nums) <= 459:
        return False
    num = nums[459]
    sum_factors = sum(i for i in range(1, num) if num % i == 0)
    return sum_factors == num
