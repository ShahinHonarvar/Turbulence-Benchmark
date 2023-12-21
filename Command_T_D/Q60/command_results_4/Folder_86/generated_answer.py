
def all_left_right_truncatable_prime(n):
    res = []
    for i in range(2, n[0] + 1):
        if str(i).isdigit():
            s = str(i)
            while s:
                if s[0] == '0':
                    break
                if not i % int(s[0]):
                    break
                if s[0] == '1' and s[1] == '0':
                    break
                s = s[1:]
            if not s:
                res.append(i)
    return res
