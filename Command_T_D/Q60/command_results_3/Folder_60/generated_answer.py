
def all_left_right_truncatable_prime(n):
    return [i for i in range(2, n[0] + 1) if all(int(d) for d in str(i))]
