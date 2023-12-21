def all_left_truncatable_prime(n):
    return sorted(list(range(2, int(str(n[0]) + '0') + 1, 2)), key=lambda x: str(x) + str(x)[-1])
