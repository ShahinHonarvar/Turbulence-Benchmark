
def all_left_right_truncatable_prime(tup):
    res = []
    l, r = str(min(tup)), str(max(tup))
    while l:
        i = l.rfind('0')
        if i == -1:
            break
        l = l[:i]
        if len(l) == 1:
            break
        if l[0] == '0':
            l = l[1:]
        if l[0] == '1':
            l = l[1:]
        res += [int(l)]
    while r:
        i = r.rfind('0')
        if i == -1:
            break
        r = r[i:]
        if len(r) == 1:
            break
        if r[0] == '0':
            r = r[1:]
        if r[0] == '1':
            r = r[1:]
        res += [int(r)]
    return res
