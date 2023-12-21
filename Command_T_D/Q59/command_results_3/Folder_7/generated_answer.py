def all_left_truncatable_prime(n):
    return sorted(
        [n for n in range(2, int(str(n).lstrip("0")) + 1) if all(int(d) > 0 for d in str(n))],
        key=lambda x: x,
    )
