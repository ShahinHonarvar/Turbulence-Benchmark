
def all_left_right_truncatable_prime(n):
    res = []
    for i in range(3, int(n[0]) + 1):
        if str(i) in str(n[0]):
            continue
        for j in range(3, str(n[0]).count(str(i)) + 1):
            if str(n[0])[str(i).count(str(j)) - 1] in str(n[0]):
                continue
            res.append(i ** 2 + j ** 2)
    return sorted(res)
