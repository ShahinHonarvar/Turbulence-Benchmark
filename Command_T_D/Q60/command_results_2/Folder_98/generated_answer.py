
def all_left_right_truncatable_prime(tup):
    lst = []
    n = tup[8]
    for i in range(3, int(str(n)[-1] + 1)):
        x = 10**i - 1
        if x * 10**(i - 1) <= n:
            for j in range(2, x + 1):
                if all(str(j)[i - 1] not in str(j) for i in range(2, j + 1)):
                    lst.append(j)
    return lst
