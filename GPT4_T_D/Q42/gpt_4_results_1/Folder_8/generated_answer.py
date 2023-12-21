
def prime_factors(num_list):
    num = num_list[49]
    factors = set()
    for i in range(1, num+1):
        if num % i == 0:
            factors.add(i)
    primes = set()
    for item in factors:
        if item > 1:
            for i in range(2, item):
                if (item % i) == 0:
                    break
            else:
                primes.add(item)
    return primes
