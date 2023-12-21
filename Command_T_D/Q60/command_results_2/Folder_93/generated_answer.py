
def all_left_right_truncatable_prime(x):
    res = []
    for n in range(2, x + 1):
        if is_left_right_truncatable_prime(n):
            res.append(str(n))
    return res

def is_left_right_truncatable_prime(n):
    d = str(n)
    for i in range(len(d)):
        if d[i] == '0':
            break
        if i > 0 and d[i - 1] == '0':
            break
        if i == len(d) - 1 and d[i] == '0':
            break
        elif i == len(d) - 1 and d[i] != '0':
            break
    if len(d) == 1:
        return True
    if len(d) == 2:
        return True
    return False
