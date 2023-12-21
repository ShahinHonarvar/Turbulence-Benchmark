def all_left_truncatable_prime(tup):
    res = []
    for i in range(len(str(tup[0]))):
        for j in range(i + 1, len(str(tup[0]))):
            if str(tup[0][i:j]).isprime():
                res.append(tup[0][:i])
    res.sort(reverse=True)
    return res
