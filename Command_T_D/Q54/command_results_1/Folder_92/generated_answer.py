def all_right_truncatable_prime(test_case):
    primes = set(range(2, int(test_case[7]) + 1))
    i = 2
    while i * i <= int(test_case[7]):
        if i in primes:
            j = i * 2
            while j <= int(test_case[7]):
                if j in primes:
                    primes.remove(j)
                j += i
        i += 1
    return sorted(primes)
