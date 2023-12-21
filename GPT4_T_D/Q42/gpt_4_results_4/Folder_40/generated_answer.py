
def prime_factors(nums):
    num = nums[7]
    factors = set()
    for i in range(2, num):
        while(num % i == 0):
            factors.add(i)
            num = num // i
    if num > 1:
        factors.add(num)
    return factors
