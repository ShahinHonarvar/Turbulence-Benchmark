
def all_left_right_truncatable_prime(l):
    res = []
    for i in range(max(l), 2, -1):
        x = str(i)
        if x[0] != '0':
            if i**2 == x[0] * x[-1]:
                res.append(i)
    return res
