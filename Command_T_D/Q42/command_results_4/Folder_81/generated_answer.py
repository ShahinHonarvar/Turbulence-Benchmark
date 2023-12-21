def prime_factors(nums):
    primes = set()
    for num in nums:
        if num < 2:
            continue
        elif num == 2 or num == 3:
            primes.add(num)
            continue
        elif num % 2 == 0 or num % 3 == 0:
            continue
        elif num == 1:
            primes.add(num)
            continue
        else:
            primes.update(prime_factors(nums[:num // 2]))
            primes.update(prime_factors(nums[num // 2 :]))
    return primes
