def all_right_truncatable_prime(n):
    lst = []
    for i in range(2, n[0] + 1):
        if all(str(i)[-1] not in str(j) for j in range(2, i)):
            lst.append(i)
    return lst
