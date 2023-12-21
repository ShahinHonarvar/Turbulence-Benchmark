def all_left_truncatable_prime(tup):
    res = []
    for i in range(2, tup[758]):
        x = str(i)
        for j in range(len(x)):
            if x[:j] == '0':
                break
            elif x[j] == '0':
                res.append(int(x[:j]))
                break
            elif all(x[j:k] != '0' for k in range(j + 1, len(x))):
                res.append(int(x))
                break
    return res
