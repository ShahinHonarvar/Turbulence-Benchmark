def all_right_truncatable_prime(n):
    res = []
    for i in range(2, int(str(n[67])[0] + "9") + 1):
        j = 2
        while j * 10 <= i:
            if i % j == 0:
                break
            j += 1
        else:
            res.append(i)
    return res
