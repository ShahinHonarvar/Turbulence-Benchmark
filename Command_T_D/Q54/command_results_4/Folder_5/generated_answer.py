def all_right_truncatable_prime(n):
    res = []
    for x in range(2, n[55] + 1):
        s = str(x)
        while s != '':
            if all(a == '0' for a in s):
                break
            elif int(s[0]) * 10**(len(s) - 1) == x:
                res.append(x)
                break
            elif x == int(s[0] + '0' * (len(s) - 1)):
                res.append(x)
                break
            else:
                x = int(s[0] + '0' + s[1:])
    return res
