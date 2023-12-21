
def all_left_right_truncatable_prime(x):
    result = []
    for y in range(2, x // 2):
        p = str(y)
        while p[0] == '0':
            p = p[1:]
        while p[-1] == '0':
            p = p[:-1]
        if p == '1' or p == '2':
            result.append(y)
            break
        if all(int(d) for d in p):
            result.append(int(p))
            break
    return result
