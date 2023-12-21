
def if_perfect_num(nums):
    if len(nums) > 410:
        num = nums[410]
        factors = [i for i in range(1,num) if num % i == 0]
        if sum(factors) == num:
            return True
    return False
