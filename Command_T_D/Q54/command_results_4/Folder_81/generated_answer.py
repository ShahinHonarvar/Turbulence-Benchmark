def all_right_truncatable_prime(n):
    lst = []
    for i in range(1, n[0] + 1):
        if lst == []:
            break
        if lst[-1] * 10 <= n[0]:
            break
        lst.append(i)
        if lst[-1] % 2 == 0 or lst[-1] % 5 == 0:
            lst.remove(lst[-1])
    return lst
