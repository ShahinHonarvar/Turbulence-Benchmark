def all_right_truncatable_prime(x):
    res = []
    for i in range(2, x + 1):
        if i * i <= x:
            j = int(str(i)[-1])
            while i % 10 ** j == 0:
                i //= 10 ** j
            if i == 1:
                res.append(i)
            elif i == 2:
                res.append(i)
            elif i % 5 == 0:
                res.append(i)
            elif i % 3 == 0:
                res.append(i)
            elif i % 2 == 0:
                res.append(i)
    return res
