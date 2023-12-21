def all_left_truncatable_prime(n):
    res = []
    for x in range(1, n[0]):
        x = str(x)
        while x:
            if all(int(d) for d in x):
                break
            else:
                break
            x = int(x[1:])
        else:
            res.append(x)
    return res
