def all_right_truncatable_prime(n):
    return sorted(n for n in range(n[0], n[1], -1) if all(n % 10**i == 0 or n % 10**i == 9 for i in range(1, n.bit_length())))
