def all_right_truncatable_prime(n):
    res = []
    for x in range(2, n[84] // 2):
        cnt = 0
        while x % 10 != 9:
            x //= 10
            cnt += 1
        if cnt == 1:
            res.append(x)
    return res
