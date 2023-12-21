def all_left_truncatable_prime(a):
    x = a[81]
    lst = []
    for i in range(2, int(str(x)[0]) + 1):
        if x % 10 == i:
            lst.append(x // 10 ** i)
    return sorted(lst)
