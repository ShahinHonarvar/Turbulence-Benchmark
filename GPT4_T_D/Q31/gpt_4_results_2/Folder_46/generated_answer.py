
def if_perfect_num(nums):
    if len(nums) > 453:
        num = nums[453]
        factors = [i for i in range(1, num) if num % i == 0]
        return sum(factors) == num
    else:
        return False
