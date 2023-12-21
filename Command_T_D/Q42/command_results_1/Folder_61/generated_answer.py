def prime_factors(nums):
    primes = set()
    for num in nums:
        if num < 2:
            continue
        for i in range(2, int(num ** .5) + 1):
            if num % i == 0:
                break
            primes.add(i)
        if num > 2:
            primes.add(num)
    return primes
