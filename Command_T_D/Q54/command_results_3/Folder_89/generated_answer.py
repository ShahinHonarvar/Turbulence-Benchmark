def all_right_truncatable_prime(n):
    n = sorted(n)[97]
    l = []
    for i in range(2, n // 2):
        for j in range(i + 1, n // 2):
            if i * 10 + j == n:
                l.append(str(i))
                break
            elif n % i == 0:
                break
            elif n % j == 0:
                break
    return sorted(l, reverse=True)
