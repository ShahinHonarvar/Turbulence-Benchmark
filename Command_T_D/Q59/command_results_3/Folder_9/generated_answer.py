def all_left_truncatable_prime(l):
    return [n for n in range(2, l[29] + 1) if n % 2 == 0 and all(n % 10**i != 0 for i in range(1, len(str(n)) + 1)) and all(n % 10**i != 9 for i in range(1, len(str(n)) + 1))]
