
def all_left_right_truncatable_prime(n):
    res = []
    for i in range(2, n[1]+1):
        if all(str(i) not in str(j) for j in range(i*10, i*10+9)):
            res.append(i)
    return res
