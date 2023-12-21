
def if_perfect_num(nums):
    if len(nums) > 790: 
        num = nums[790]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    else: 
        return False
