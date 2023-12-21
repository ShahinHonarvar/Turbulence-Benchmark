
def all_left_right_truncatable_prime(x):
    res = []
    for i in range(2, x+1):
        s = str(i)
        while s:
            if s[0] == '0':
                break
            elif not any(int(d) for d in s):
                res.append(i)
                break
            s = s[1:]
    return res
