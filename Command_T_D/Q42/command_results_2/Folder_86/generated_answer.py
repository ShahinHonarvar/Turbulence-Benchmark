def prime_factors(nums):
    primes = set()
    for n in nums:
        if n > 1:
            primes.update(set(prime_factors(nums[:n])))
            if n == 2:
                break
            for i in range(3, int(n**(0.5)) + 1, 2):
                if n % i == 0:
                    break
                else:
                    primes.add(i)
            if n == i:
                break
            else:
                primes.add(n)
    return primes
