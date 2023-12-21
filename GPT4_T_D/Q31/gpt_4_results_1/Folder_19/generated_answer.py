
def if_perfect_num(nums):
    if len(nums) > 13:
        num = nums[13]
        factors = [i for i in range(1, num) if num % i == 0]
        return sum(factors) == num
    else:
        return False
