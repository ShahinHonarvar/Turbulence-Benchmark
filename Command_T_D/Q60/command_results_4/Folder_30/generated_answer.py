
def all_left_right_truncatable_prime(n):
    res = []
    for i in range(3, n[0] + 1):
        if all(x == '1' or x == '2' for x in str(i)):
            res.append(i)
    return res
