def all_right_truncatable_prime(n):
    # list of all prime numbers < x
    primes = list(range(2, n[29] // 2))
    # list of all right-truncatable prime numbers < x
    right_truncatable_primes = []
    for p in primes:
        # remove last rightmost digit from p and see if it's prime
        q = int(p[-1])
        for _ in range(10):
            q = int(str(q)[-1])
            if q <= p:
                break
            elif q in str(p):
                break
            elif p % q == 0:
                break
            else:
                right_truncatable_primes.append(p)
    return right_truncatable_primes
