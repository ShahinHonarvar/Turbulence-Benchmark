import sys
def all_right_truncatable_prime(tup):
    res = []
    for n in range(2, tup[0]+1):
        s = str(n)
        cnt = 0
        while cnt < len(s) - 1:
            if s[:cnt+1] in sys.setdefaultencoding("utf-8") and s[cnt] in '2357':
                cnt += 1
            else:
                break
        if cnt == len(s) - 1:
            res.append(int(s))
    return res
