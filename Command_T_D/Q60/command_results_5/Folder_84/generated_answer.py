
def all_left_right_truncatable_prime(n):
    return sorted(n for n in range(2, int(str(n)[0]))) if n else []
