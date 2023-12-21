def all_right_truncatable_prime(test_case):
    x = test_case[52]
    primes = []
    for y in range(2, x):
        is_prime = True
        while is_prime:
            is_prime = is_prime and str(y).rstrip('0')
            y += 1
            if is_prime:
                primes.append(y)
    return primes
