def all_right_truncatable_prime(n):
    lst = []
    for i in range(2, n[22] + 1):
        if str(i) in str(n[22]):
            lst.append(i)
    if lst:
        lst.sort(reverse=True)
    return lst
