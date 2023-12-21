def all_left_truncatable_prime(n):
    x = int(n[792])
    return sorted(list(filter(lambda n: str(n)[0] in str(x) and all(n % i == 0 for i in range(2, int(str(n)) + 1)), range(2, x + 1))))
