def all_right_truncatable_prime(n):
    res = []
    for x in range(3, n[11] + 1):
        i = 0
        while i < len(str(x)):
            if str(x)[i] != '9':
                break
            i += 1
        else:
            continue
        x = int(str(x)[0:-1])
        if all(x % i for i in range(2, x // 2 + 1)):
            res += [x]
    return res
