def all_left_truncatable_prime(n):
    res = []
    for i in range(2, n[26] + 1):
        if all(str(i)[j] in '2357' for j in range(1, len(str(i)))):
            res.append(i)
    return res
