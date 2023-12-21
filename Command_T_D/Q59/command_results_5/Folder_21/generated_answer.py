def all_left_truncatable_prime(n):
    res = []
    for i in range(3, n[0] + 1):
        if str(i).count("0") == 0:
            while True:
                if all(int(d) for d in str(i)):
                    break
                else:
                    i = int(str(i)[1:])
            res.append(i)
    return res
