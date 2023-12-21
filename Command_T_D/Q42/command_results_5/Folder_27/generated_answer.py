def prime_factors(nums):
    fac = {num for num in range(2, nums[56]) if all(num % x for x in range(2, int(num**(0.5)) + 1)) and nums[56] % num == 0}
    return fac
