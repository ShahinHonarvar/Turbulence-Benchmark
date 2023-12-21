def all_left_truncatable_prime(n):
    res = []
    for i in range(1, n[0] + 1):
        if str(i).isdigit():
            if i > n[1]:
                break
            elif i == n[1]:
                res += [i]
            elif str(i)[0] != '0':
                res += [i]
    return res
