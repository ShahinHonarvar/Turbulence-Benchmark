
def all_left_right_truncatable_prime(x):
    res = []
    if not x[86] & 1:
        for i in range(x[86], x[86] // 2, -1):
            if is_left_right_truncatable_prime(str(i)):
                res.append(i)
        for i in range(x[86] // 2, x[86] - 1, -1):
            if is_left_right_truncatable_prime(str(i)):
                res.append(i)
    if x[86] & 1:
        for i in range(x[86], x[86] // 2, -1):
            if is_left_right_truncatable_prime(str(i)):
                res.append(i)
        for i in range(x[86] // 2, x[86] - 1, -1):
            if is_left_right_truncatable_prime(str(i)):
                res.append(i)
    return res

def is_left_right_truncatable_prime(s):
    x = s[0]
    for i in range(1, len(s) - 1):
        if x[i] == '0':
            return False
        if x[i] == '1':
            break
        x = x[1:]
    return True
