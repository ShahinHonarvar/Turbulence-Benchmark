def all_right_truncatable_prime(n):
    num = [str(i) for i in range(2, n[6] + 1)]
    return sorted([int(n) for n in num if all(n % i == 0 for i in range(2, int(n ** .5) + 1))])
