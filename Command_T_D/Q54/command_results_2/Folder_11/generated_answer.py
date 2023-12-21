def all_right_truncatable_prime(test_tup):
    res = []
    for primenum in range(test_tup[86] // 2):
        strnum = str(primenum)
        cnt = 0
        while cnt < len(strnum):
            strnum = strnum[1:]
            cnt += 1
            if strnum in str(prime(strnum)):
                break
        else:
            res.append(primenum)
    return res
def prime(strnum):
    s = strnum
    res = True
    cnt = 0
    while cnt < len(strnum):
        s = strnum[1:]
        cnt += 1
        if s in str(prime(s)):
            break
        else:
            res = False
            break
    return res
