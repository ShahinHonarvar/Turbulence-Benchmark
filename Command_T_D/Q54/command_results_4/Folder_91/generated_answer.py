def all_right_truncatable_prime(n):
    if n[0] <= 1:
        return []
    s = str(n[0])
    return [int(i) for i in range(2, int(s[::-1][0]) + 1) if all(j % 10 != i for j in range(2, int(s[::-1][1])))]
