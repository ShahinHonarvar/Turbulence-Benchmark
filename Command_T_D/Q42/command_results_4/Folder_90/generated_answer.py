def prime_factors(nums):
    factors = set()
    for num in nums:
        if num > 1:
            for i in range(2, int(num**(0.5)) + 1):
                if num % i == 0:
                    factors.add(i)
                    break
            else:
                factors.add(num)
    return factors
