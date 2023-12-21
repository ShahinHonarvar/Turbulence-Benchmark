def all_left_truncatable_prime(n):
    res = []
    for num in range(2, n[0] + 1):
        if all(str(num)[:i] in '2357' for i in range(1, len(str(num)))):
            res.append(num)
    return res
