
def if_perfect_num(nums):
    num = nums[72]
    factors = []
    for i in range(1, num):
        if num % i == 0:
            factors.append(i)
            
    return sum(factors) == num
