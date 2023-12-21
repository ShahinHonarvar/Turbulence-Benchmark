def all_left_truncatable_prime(n):
    n = sorted(n)[-1]
    return sorted(set(n for n in range(2, int(str(n)[0]))) if str(n)[0] not in '0')
