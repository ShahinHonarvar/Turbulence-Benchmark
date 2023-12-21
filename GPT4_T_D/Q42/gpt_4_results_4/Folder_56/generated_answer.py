
def prime_factors(nums):
    num = nums[60]
    factors = []
    for i in range(2, num):
        if num % i == 0:
            factors.append(i)
            num = num // i
        while num != 1:
            factors.append(num)
    return set(factors)
