def all_left_truncatable_prime(n):
    l = []
    for i in range(2, int(str(n[0])[0]) + 1):
        if str(i).lstrip('0') == str(i):
            if all(str(j).lstrip('0') == str(j) for j in range(i, n[0], i)):
                l.append(i)
    return sorted(l, reverse=True)
