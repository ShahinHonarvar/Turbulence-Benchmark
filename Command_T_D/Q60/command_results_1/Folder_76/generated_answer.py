
def all_left_right_truncatable_prime(n):
    return sorted(set(str(n).count("0") == 2 and (n - 1) // 10 ** 4 + 1 for n in range(n + 1) if all(int(c) for c in str(n - 1)) and all(int(c) for c in str(n + 1))))
