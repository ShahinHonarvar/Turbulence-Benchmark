def prime_factors(nums):
    primes = set()
    for num in nums:
        if num == 1:
            continue
        for i in range(2, int(num ** .5) + 1):
            if num % i == 0:
                primes.add(i)
                break
        else:
            primes.add(num)
    return primes
