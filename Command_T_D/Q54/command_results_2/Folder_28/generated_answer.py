import bisect
def all_right_truncatable_prime(n):
    res = []
    for i in range(2, n[19]):
        j = str(i)
        while j:
            if j[-1] == '9':
                break
            elif j[-1] == '0':
                return res
            elif i % 10 == 0:
                continue
            elif str(i - 1) == str(i)[:-1]:
                continue
            elif str(i - 1) == str(i):
                break
            else:
                res.append(i)
                break
    return res
