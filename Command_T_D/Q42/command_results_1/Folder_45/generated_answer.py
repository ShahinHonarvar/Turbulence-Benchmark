def prime_factors(nums):
    factors = set()
    for num in nums:
        if num > 1:
            for i in range(2, int(num**(0.5)) + 1):
                if num % i == 0:
                    factors.add(i)
                    while num % i == 0:
                        num /= i
                    if num > 1:
                        factors.add(num)
                        break
    return factors
