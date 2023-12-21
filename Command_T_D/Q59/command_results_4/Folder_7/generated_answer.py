def all_left_truncatable_prime(test_case):
    primes = []
    for p in range(2, test_case[803] + 1):
        if all(p % n != 0 for n in range(2, int(str(p)[-1]))) and p not in primes:
            primes.append(p)
    return sorted(primes)
