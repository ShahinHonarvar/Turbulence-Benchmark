def all_left_truncatable_prime(n):
    lst = []
    for i in range(2, int(str(n)[-1]) + 1):
        p = str(i)
        for j in range(1, len(p)):
            if p[j] == '0':
                break
            elif p[j] == '1':
                continue
            else:
                break
        else:
            if int(p[0]) < int(str(n)[-1]):
                lst.append(int(p))
    return lst
