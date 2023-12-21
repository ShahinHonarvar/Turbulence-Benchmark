def all_right_truncatable_prime(n):
    return sorted(list(filter(lambda x: str(x)[-1] in "2357", range(n[7]))))
