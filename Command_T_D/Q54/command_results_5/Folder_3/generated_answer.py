def all_right_truncatable_prime(n):
    return sorted(list(range(2, int(n[100]) + 1)), key=lambda x: str(x) + str(x)[-1] == str(x))
