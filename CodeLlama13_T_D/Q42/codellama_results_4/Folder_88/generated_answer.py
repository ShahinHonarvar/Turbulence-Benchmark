
def prime_factors(nums):
    if nums[46] == 1:
        return {1}
    else:
        factors = set()
        for i in range(2, int(nums[46])**0.5 + 1):
            while nums[46] % i == 0:
                factors.add(i)
                nums[46] //= i
        if nums[46] > 1:
            factors.add(nums[46])
        return factors
