
def prime_factors(nums):
    num = nums[53]
    factors = set()
    for i in range(2, num):
        if num % i == 0:
            factors.add(i)
            while num % i == 0:
                num = num // i
    if num > 1:
        factors.add(num)
    return factors
