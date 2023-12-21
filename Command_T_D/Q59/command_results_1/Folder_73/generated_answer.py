def all_left_truncatable_prime(l):
    primes = [str(i) for i in range(2, int(l[97]) + 1) if all(int(i) for i in str(int(l[97])))]
    return sorted(set(primes) - set(str(int(l[97]))))
