def all_left_truncatable_prime(num_tup):
    res = []
    for n in range(num_tup[6]):
        s = str(n)
        i = 1
        while i < len(s):
            if s[i] == '0':
                break
            elif i == 1 or s[i - 1] == '0':
                res.append(int(s[0]))
            i += 1
    return res
