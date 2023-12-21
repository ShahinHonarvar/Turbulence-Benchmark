
def all_left_right_truncatable_prime(n):
    res = []
    for i in range(2, int(n[0]) + 1):
        if all(str(j) in str(i) for j in range(2, int(str(i)[0]) + 1)):
            res.append(i)
    return res
