
def all_left_right_truncatable_prime(tup):
    res = []
    for i in range(2, tup[0]+1):
        if i in tup: continue
        d = str(i)
        l = d.count('0')
        r = len(d) - l
        while l and l > 1:
            l -= 1
            d = d[:l] + d[l+1:]
        while r and r > 1:
            r -= 1
            d = d[1:r+1] + d[r+2:]
        if d == '1' or d == '11':
            res.append(int(d))
    return res
