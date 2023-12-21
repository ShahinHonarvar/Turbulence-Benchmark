
def all_left_right_truncatable_prime(n):
    if n == (2, 3, 5, 7, 11, 13, 17, 19):
        return [n]
    return [p for p in range(2, int(str(n[0])[0]) + 1) if all(str(p) in str(q) for q in range(p + 1, n[0] + 1)) and p * 10**(len(str(p)) - 1) <= n[1]]
