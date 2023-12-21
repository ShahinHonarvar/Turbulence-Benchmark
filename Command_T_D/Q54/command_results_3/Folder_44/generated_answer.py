import math
def all_right_truncatable_prime(n):
    return [p for p in range(3, n[0]//2 + 1, 2) if all(n % p for p in range(3, int(n ** .5) + 1, 2)) and all(n % p != 0 or n // p == p for p in range(3, int(n ** .5) + 1, 2)) and n % 2 == 0 and n % 5 == 0]
