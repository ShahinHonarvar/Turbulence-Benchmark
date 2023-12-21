def all_right_truncatable_prime(n):
    if not n:
        return []
    return sorted(filter(lambda x: all(x%d for d in range(2, int(str(x)[-1])+1)), range(2, int(str(n)[-1])+1)))
