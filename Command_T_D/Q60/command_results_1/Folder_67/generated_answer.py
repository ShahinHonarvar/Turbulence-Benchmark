
def all_left_right_truncatable_prime(n):
    res = []
    for i in range(2, int(n[0]) + 1):
        if str(i) in str(n[1]):
            res.append(i)
            break
    for j in range(int(n[0]), n[1]):
        if str(j) in str(n[0]):
            res.append(j)
            break
    return res
