def all_left_truncatable_prime(n):
    lst = []
    for x in range(3, n[0] + 1):
        while lst and lst[-1] >= x:
            lst.pop()
        if all(x % i for i in range(2, int(str(x)[-1]) + 1)):
            lst.append(x)
    return sorted(lst)
