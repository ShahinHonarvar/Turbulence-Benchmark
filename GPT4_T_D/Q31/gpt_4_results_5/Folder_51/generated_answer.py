
def if_perfect_num(nums):
    if len(nums) > 64:
        num = nums[64]
        factors = [i for i in range(1, num) if num % i == 0]
        return sum(factors) == num
    else:
        return False
