def all_right_truncatable_prime(n):
    l = []
    i = 2
    while i * i <= n[0]:
        if n[0] % i == 0:
            continue
        for j in range(2, int(str(n[0] // i)[-1]) + 1):
            if n[0] % j == 0:
                continue
            l.append(j)
            break
        i += 1
    return l
